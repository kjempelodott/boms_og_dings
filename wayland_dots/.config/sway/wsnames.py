#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import os
from i3ipc import Connection, Event

max_length = 30
i3 = Connection(os.environ.get('SWAYSOCK'), auto_reconnect=True)

def rename(con, e):
    ws = con.workspace()
    name = con.name if len(con.name) <= max_length else con.name[:max_length - 1] + '…'
    name = f'{ws.num}: {name}'
    if name == ws.name:
        return
    command = 'rename workspace "{}" to "{}"'.format(ws.name.replace('"', '\\"'),
                                                     name.replace('"', '\\"'))
    i3.command(command)

def assign_name(i3, e):
    if not e.change == 'rename':
        try:
            con = i3.get_tree().find_focused()
            if not con.type == 'workspace':
                if e.change in ('focus', 'title'):
                    rename(con, e)
                elif e.change == 'new':
                    con = i3.get_tree().find_by_id(e.container.id)
                    rename(con, e)
        except Exception as ex:
            exit(ex)

def main():
    # Subscribe to events
    i3.on(Event.WORKSPACE_FOCUS, assign_name)
    i3.on(Event.WINDOW_FOCUS, assign_name)
    i3.on(Event.WINDOW_TITLE, assign_name)
    i3.on(Event.WINDOW_CLOSE, assign_name)
    i3.on(Event.WINDOW_NEW, assign_name)
    i3.on(Event.BINDING, assign_name)
    i3.main()

if __name__ == "__main__":
    main()
