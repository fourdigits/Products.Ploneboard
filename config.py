from PloneboardPermissions import AddBoard, AddForum, AddConversation, AddComment

ADD_BOARD_PERMISSION = AddBoard
ADD_FORUM_PERMISSION = AddForum
ADD_CONVERSATION_PERMISSION = AddConversation
ADD_COMMENT_PERMISSION = AddComment
PROJECTNAME = "Ploneboard"
SKINS_DIR = 'skins'
EMOTICON_TRANSFORM_ID = 'text_to_emoticons'
EMOTICON_TRANSFORM_MODULE = 'Products.Ploneboard.transforms.text_to_emoticons'
URL_TRANSFORM_MODULE = 'Products.Ploneboard.transforms.url_to_hyperlink'
PLONEBOARD_TRANSFORMSCHAIN_ID = 'ploneboard_chain'
PLONEBOARD_TOOL = 'portal_ploneboard'
GLOBALS = globals()
