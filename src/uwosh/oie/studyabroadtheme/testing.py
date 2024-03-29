from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import (
    FunctionalTesting,
    IntegrationTesting,
    PloneSandboxLayer,
    applyProfile,
)
from plone.testing.z2 import ZSERVER_FIXTURE

import uwosh.oie.studyabroadtheme


class UwoshOieStudyabroadthemeLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=uwosh.oie.studyabroadtheme)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'uwosh.oie.studyabroadtheme:default')


UWOSH_OIE_STUDYABROADTHEME_FIXTURE = UwoshOieStudyabroadthemeLayer()


UWOSH_OIE_STUDYABROADTHEME_INTEGRATION_TESTING = IntegrationTesting(
    bases=(UWOSH_OIE_STUDYABROADTHEME_FIXTURE,),
    name='UwoshOieStudyabroadthemeLayer:IntegrationTesting',
)


UWOSH_OIE_STUDYABROADTHEME_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(UWOSH_OIE_STUDYABROADTHEME_FIXTURE,),
    name='UwoshOieStudyabroadthemeLayer:FunctionalTesting',
)


UWOSH_OIE_STUDYABROADTHEME_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        UWOSH_OIE_STUDYABROADTHEME_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        ZSERVER_FIXTURE,
    ),
    name='UwoshOieStudyabroadthemeLayer:AcceptanceTesting',
)
