# -*- coding: utf-8 -*-

import dolmen.content as dolmen
from zope.interface import implements
from zope.i18nmessageid import MessageFactory
from zope.schema.fieldproperty import FieldProperty
from dolmen.app.content import IDynamicLayout

_ = MessageFactory('dolmen')


class IFolder(IDynamicLayout):
    """Marker interface for folders.
    """


class Folder(dolmen.Container):
    implements(IFolder)
    dolmen.name(_(u"Folder"))
    dolmen.icon("folder.png")

    layout = FieldProperty(IFolder['layout'])
