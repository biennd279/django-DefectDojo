from dojo.models import System_Settings

from .dojo_test_case import DojoTestCase


class TestSystemSettings(DojoTestCase):

    def test_system_settings_update(self):
        try:
            # although the unittests are run after initial data has been loaded, for some reason in cicd sometimes the settings aren't present
            system_settings = System_Settings.objects.get()
        except System_Settings.DoesNotExist:
            system_settings = System_Settings()

        system_settings.enable_jira = True
        system_settings.save()
        system_settings = System_Settings.objects.get()
        self.assertEqual(system_settings.enable_jira, True)

        system_settings.enable_jira = False
        system_settings.save()
        system_settings = System_Settings.objects.get()
        self.assertEqual(system_settings.enable_jira, False)

        system_settings.enable_jira = True
        system_settings.save()
        system_settings = System_Settings.objects.get(no_cache=True)
        self.assertEqual(system_settings.enable_jira, True)
