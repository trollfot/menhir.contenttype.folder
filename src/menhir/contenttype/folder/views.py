import grok
from base import IFolder
from megrok.z3cform.base import IGrokForm
from dolmen.app.container import listing
from dolmen.app.viewselector import AlternativeView
from zope.component import getMultiAdapter

grok.context(IFolder)


class ContentListingView(listing.FolderListing, AlternativeView):
    grok.name('listing')
    grok.title('Content of the folder')
    

class CompositeView(AlternativeView):
    grok.title('Summary view')

    def update(self):
        self.items = []
        for item in self.context.values():
            view = getMultiAdapter((item, self.request), name="index")
            view.update()
            if IGrokForm.providedBy(view): view.updateForm()
            self.items.append(view.content())
