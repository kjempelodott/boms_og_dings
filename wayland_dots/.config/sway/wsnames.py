#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

from i3ipc import Connection, Event

max_length = 30
i3 = Connection()

def assign_generic_name(i3, e):
    if not e.change == 'rename':
        try:
            con = i3.get_tree().find_focused()
            if not con.type == 'workspace':
                if not e.change == 'new':
                    ws_old_name = con.workspace().name
                    ws_name = "%s: %s" % (con.workspace().num, con.name)
                    name = ws_name if len(ws_name) <= max_length else ws_name[:max_length - 1] + "…"
                    i3.command('rename workspace "%s" to %s' % (ws_old_name, name))
                else:
                    con = i3.get_tree().find_by_id(e.container.id)
                    ws_num = con.workspace().num
                    w_name = con.name if con.name else ''
                    if w_name and ws_num:
                        name = "%s: %s" % (ws_num, w_name)
                        i3.command('rename workspace "%s" to %s' % (ws_num, name))
            else:
                ws_num = con.workspace().num
                ws_new_name = "%s:" % ws_num
                i3.command('rename workspace to "{}"'.format(ws_new_name))
        except Exception as ex:
            exit(ex)

def main():
    # Subscribe to events
    i3.on(Event.WORKSPACE_FOCUS, assign_generic_name)
    i3.on(Event.WINDOW_FOCUS, assign_generic_name)
    i3.on(Event.WINDOW_TITLE, assign_generic_name)
    i3.on(Event.WINDOW_CLOSE, assign_generic_name)
    i3.on(Event.WINDOW_NEW, assign_generic_name)
    i3.on(Event.BINDING, assign_generic_name)
    i3.main()

if __name__ == "__main__":
    main()
