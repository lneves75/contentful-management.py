import vcr
from unittest import TestCase
from contentful_management.content_type_editor_interfaces_proxy import ContentTypeEditorInterfacesProxy
from .test_helper import CLIENT, PLAYGROUND_SPACE


class ContentTypeEditorInterfacesProxyTest(TestCase):
    def test_content_type_editor_interfaces_proxy(self):
        proxy = ContentTypeEditorInterfacesProxy(CLIENT, PLAYGROUND_SPACE, 'foo')

        self.assertEqual(str(proxy), "<ContentTypeEditorInterfacesProxy space_id='{0}' content_type_id='foo'>".format(PLAYGROUND_SPACE))

        with self.assertRaises(Exception):
            proxy.create()

        with self.assertRaises(Exception):
            proxy.delete()

    @vcr.use_cassette('fixtures/editor_interface/all.yaml')
    def test_content_type_editor_interfaces_proxy_all(self):
        proxy = ContentTypeEditorInterfacesProxy(CLIENT, PLAYGROUND_SPACE, 'foo')

        editor_interface = proxy.all()

        self.assertTrue(editor_interface)
        self.assertTrue(editor_interface.id)

    @vcr.use_cassette('fixtures/editor_interface/all.yaml')
    def test_content_type_editor_interfaces_proxy_find(self):
        proxy = ContentTypeEditorInterfacesProxy(CLIENT, PLAYGROUND_SPACE, 'foo')

        editor_interface = proxy.find()

        self.assertTrue(editor_interface)
        self.assertTrue(editor_interface.id)
