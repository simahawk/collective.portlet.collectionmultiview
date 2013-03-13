from zope.app.form.browser.widget import SimpleInputWidget
try:
    import plone.app.upgrade
    from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
except ImportError:
    from zope.app.pagetemplate.viewpagetemplatefile import ViewPageTemplateFile
from zope.formlib import form
try:
    from zope.formlib.widget import BrowserWidget
except ImportError:
    # Plone 3
    from zope.app.form.browser import BrowserWidget
try:
    from zope.formlib.widget import InputWidget
except ImportError:
    # Plone 3
    from zope.app.form import InputWidget

from collective.portlet.collectionmultiview.interfaces import (
    ICollectionMultiViewRenderer
)

class RendererSelectWidget(SimpleInputWidget):

    template = ViewPageTemplateFile('rendererselectwidget.pt')

    def __call__(self):
        value = self._getFormValue()
        return self.template(
            field=self.context,
            name=self.name,
            value=value,
            script=self.script(),
        )

    def script(self):
        return '''
        var reloadRenderer = function () {
            $('[name="%(name)s.reload"]').click();
        }
        ''' % {'name':self.name}
