# -*- coding:utf-8 -*-
from plone.app.testing import (
    PloneSandboxLayer,
    PLONE_FIXTURE,
    IntegrationTesting,
    FunctionalTesting,
)
from plone.testing import z2
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE


class LayoutsTests(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        import collective.layouts
        self.loadZCML(package=collective.layouts)

    def setUpPloneSite(self, portal):
        portal.portal_workflow.setDefaultChain('simple_publication_workflow')
        self.applyProfile(
            portal, 'collective.layouts:default')


LAYOUTS_FIXTURE = LayoutsTests()

LAYOUTS_INTEGRATION_TESTING = IntegrationTesting(
    bases=(LAYOUTS_FIXTURE,),
    name='LayoutsTests:Integration')

LAYOUTS_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(LAYOUTS_FIXTURE,),
    name='LayoutsTests:Functional')

LAYOUTS_ROBOT_TESTING = FunctionalTesting(
    bases=(LAYOUTS_FIXTURE,
           REMOTE_LIBRARY_BUNDLE_FIXTURE,
           z2.ZSERVER),
    name='LayoutsTests:Robot')
