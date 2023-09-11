#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import os, re
from i3ipc import Connection, Event

max_length = 30
i3 = Connection(os.environ.get('SWAYSOCK'), auto_reconnect=True)
repl = re.compile(r'([\'\"])')

def rename(con, e):
    ws = con.workspace()
    name = con.name if len(con.name) <= max_length else con.name[:max_length - 1] + '…'
    if name == ws.name:
        return
    name = f'{ws.num}: {name}'
    command = 'rename workspace "{}" to "{}"'.format(repl.sub(r'\1', ws.name), repl.sub(r'\1', name))
    res = i3.command(command)

def assign_name(i3, e):
    if not e.change == 'rename':
        try:
            con = i3.get_tree().find_focused()
            if con is None:
                return
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
