# -*- coding: utf-8 -*-

import grok
import dolmen.content

from zope.interface import implements
from zope.i18nmessageid import MessageFactory
from zope.schema.fieldproperty import FieldProperty
from dolmen.app.viewselector import IViewSelector

_ = MessageFactory('dolmen')


class IFolder(IViewSelector):
    """Marker interface for folders.
    """


class Folder(dolmen.content.Container):
    grok.implements(IFolder)
    dolmen.content.name(_(u"Folder"))
    dolmen.content.icon("folder.png")

    selected_view = FieldProperty(IFolder['selected_view'])
