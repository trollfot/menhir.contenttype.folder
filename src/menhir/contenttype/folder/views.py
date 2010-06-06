#!/usr/bin/python
# -*- coding: utf-8 -*-

import grok
from dolmen import menu
from dolmen.app.container import listing
from dolmen.app.layout import Page
from dolmen.app.viewselector import SelectableViewsMenu
from megrok.z3cform.base import IGrokForm
from menhir.contenttype.folder import IFolder
from zope.component import getMultiAdapter


@menu.menuentry(SelectableViewsMenu)
class ContentListingView(listing.FolderListing):
    grok.name('listing')
    grok.context(IFolder)
    grok.title('Content of the folder')


@menu.menuentry(SelectableViewsMenu)
class CompositeView(Page):
    grok.context(IFolder)
    grok.title('Summary view')

    def update(self):
        self.items = []
        for item in self.context.values():
            view = getMultiAdapter((item, self.request), name="index")
            view.update()
            if IGrokForm.providedBy(view): view.updateForm()
            self.items.append(view.content())
