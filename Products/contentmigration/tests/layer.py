# from Products.PloneTestCase.layer import PloneSite

# # BBB Zope 2.12
# try:
#     from Zope2.App import zcml
#     from OFS import metaconfigure
#     zcml, metaconfigure  # pyflakes
# except ImportError:
#     from Products.Five import zcml
#     from Products.Five import fiveconfigure as metaconfigure


# class TestLayer(PloneSite):
#     """ layer for integration tests """

#     @classmethod
#     def setUp(cls):
#         metaconfigure.debug_mode = True
#         from Products import contentmigration
#         zcml.load_config('testing.zcml', package=contentmigration)
#         metaconfigure.debug_mode = False

#     @classmethod
#     def tearDown(cls):
#         pass


# class SchemaExtenderTestLayer(PloneSite):
#     """ layer for integration tests with archetypes.schemaextender """

#     @classmethod
#     def setUp(cls):
#         metaconfigure.debug_mode = True
#         from Products import contentmigration
#         zcml.load_config('testing.zcml', package=contentmigration)
#         zcml.load_config('testing-schemaextender.zcml',
#                          package=contentmigration)
#         metaconfigure.debug_mode = False

#     @classmethod
#     def tearDown(cls):
#         pass


from plone.app.testing import bbb
from plone.app import testing


class PloneTestCaseFixture(bbb.PloneTestCaseFixture):

    defaultBases = (bbb.PTC_FIXTURE, )

    def setUpZope(self, app, configurationContext):
        from Products import contentmigration
        self.loadZCML('testing.zcml', package=contentmigration)
        self.loadZCML('testing-schemaextender.zcml', package=contentmigration)

PCM_FIXTURE = PloneTestCaseFixture()
TestLayer = testing.FunctionalTesting(
    bases=(PCM_FIXTURE, ), name='PloneContentMigrationTestCase:Functional')

SchemaExtenderTestLayer = TestLayer
