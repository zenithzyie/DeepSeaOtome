################################################################################
## Save and Load screens #######################################################
################################################################################

screen save():

    tag menu

    use file_slots(_("Save"))


screen load():

    tag menu

    use file_slots(_("Load"))


screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))

    use game_menu_prefs(title):

        fixed:

            ## This ensures the input will get the enter event before any of the
            ## buttons do.
            order_reverse True

            ## The page name, which can be edited by clicking on a button.
            # button:
            #     #style "page_label"

            #     key_events True
            #     xalign 0.5
            #     action page_name_value.Toggle()

            #     input:
            #         style "page_label_text"
            #         value page_name_value

            ## The grid of file slots.
            vpgrid:
                cols gui.file_slot_cols
                rows gui.file_slot_rows
                spacing gui.slot_spacing
                draggable True
                mousewheel True
                scrollbars "vertical"
                style_prefix "slot"

                xalign 0.5
                #yalign 0.5
                xysize (984, 489)

                #spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    hbox:
                        #null width (20 * gui.pref_spacing)
                        button:
                            action FileAction(slot)
                            vbox:
                                text [str(slot)]:
                                    style "slot_time_text"
                                    xpos 30
                                    ypos 40
                            vbox:
                                add FileScreenshot(slot) size (169, 88) ypos 8
                                #xalign 0.5
                                xpos 60

                            vbox:
                                text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                                    style "slot_time_text"
                                    xpos 325
                                    ypos 45

                                text FileSaveName(slot):
                                    style "slot_name_text"

                                key "save_delete" action FileDelete(slot)
                        null width (15 * gui.pref_spacing)

            # ## Buttons to access other pages.
            # vbox:
            #     style_prefix "page"

            #     xalign 0.5
            #     yalign 1.0

            #     hbox:
            #         xalign 0.5

            #         spacing gui.page_spacing

            #         #textbutton _("<") action FilePagePrevious()

            #         if config.has_autosave:
            #             textbutton _("{#auto_page}A") action FilePage("auto")

            #         #if config.has_quicksave:
            #             #textbutton _("{#quick_page}Q") action FilePage("quick")

            #         ## range(1, 10) gives the numbers from 1 to 9.
            #         for page in range(1, 4):
            #             textbutton "[page]" action FilePage(page)

            #         #textbutton _(">") action FilePageNext()

            #     if config.has_sync:
            #         if CurrentScreenName() == "save":
            #             textbutton _("Upload Sync"):
            #                 action UploadSync()
            #                 xalign 0.5
            #         else:
            #             textbutton _("Download Sync"):
            #                 action DownloadSync()
            #                 xalign 0.5


style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
#style slot_time_text is slot_button_text
style slot_time_text:
    size 25
style slot_name_text is slot_button_text

style page_label:
    xpadding 50
    ypadding 3

style page_label_text:
    textalign 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.text_properties("slot_button")
