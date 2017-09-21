"""perso URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url

from apps.config.view import TreeViews
from apps.config.view import FeatureViews
from apps.config.view import views
from apps.config.view import MainViews
from apps.config.view import RoConfigViews
from apps.config.view import XmlConfigViews
from apps.config.view import ProviderViews
from apps.config.view import HardWareViews
from apps.config.view import JenkinsViews
from apps.config.view import DifferenceViews
from apps.config.view import VersionDifferenceView
from apps.config.view import WorkspaceViews
from apps.config.view import VisualAppViews
from apps.config.view import CountOrderViews


urlpatterns = [
    url(r'^to_deploy', MainViews.to_deploy),
    url(r'^to_copy_order', views.to_copy_order),
    url(r'^to_add_order', views.to_add_order),
    url(r'^to_requirement_list', views.to_requirement_list),
    url(r'^to_feature_modal', FeatureViews.to_feature_modal),
    url(r'^to_resource_modal', views.to_resource_modal),
    url(r'^to_resource_edit', views.to_resource_edit),
    url(r'^selectRequirement', views.selectRequirement),
    url(r'^show_fileUpload', views.show_fileUpload),
    url(r'^fileUpload', views.file_upload),
    url(r'^queryResourceModalInfo', views.queryResourceModalInfo),
    url(r'^queryResourceById', views.queryResourceById),
    url(r'^downloadResourceById', views.downloadResourceById),
    url(r'^showFileView', views.show_fileView),
    url(r'^update_resource_info', views.update_resource_info),
    url(r'^showPicView', views.show_picView),
    url(r'^upload_file', views.upload_file),
    url(r'^ajaxQueryJiraKeys', views.ajaxQueryJiraKeys),
    url(r'^queryAllProjectInfos', views.queryAllProjectInfos),
    url(r'^queryProjectResourceInfos', views.queryProjectResourceInfos),
    url(r'^queryCustomerAndRegionById', views.queryCustomerAndRegionById),
    url(r'^queryJiraKeyNameById', views.queryJiraKeyNameById),
    url(r'^queryResourceWithProject', views.queryResourceWithProject),
    url(r'^downloadResourceByFtp', views.downloadResourceByFtp),
    url(r'^queryPublishState', views.queryPublishState),
    url(r'^queryResourceUsedCount', views.queryResourceUsedCount),
    url(r'^delResourceById', views.delResourceById),
    url(r'^queryRequirementType', views.queryRequirementType),

    url(r'^refresh_svr_directory', TreeViews.refresh_svr_directory),
    url(r'^get_svr_tree', TreeViews.get_svr_tree),
    url(r'^toConfig', TreeViews.to_config),
    url(r'^load_module', TreeViews.load_module),
    url(r'^load_target_module', TreeViews.load_target_module),

    url(r'^load_requirement', FeatureViews.load_requirement),
    url(r'^save_ro_config', FeatureViews.save_ro_config),
    url(r'^save_xml_config', FeatureViews.save_xml_config),
    url(r'^generate_main_code_bin', MainViews.generate_main_code_bin),
    url(r'^to_jenkins_notification', MainViews.to_jenkins_notification),

    url(r'^to_roconfig_modal', RoConfigViews.to_roconfig_modal),
    url(r'^roconfig_load_requirement', RoConfigViews.load_requirement),
    url(r'^roconfig_save_ro_config', RoConfigViews.save_ro_config),
    url(r'^roconfig_save_xml_config', RoConfigViews.save_xml_config),

    url(r'^to_hardware_modal', HardWareViews.to_hardware_modal),
    url(r'^hardware_load_requirement', HardWareViews.load_requirement),
    url(r'^hardware_save_ro_config', HardWareViews.save_ro_config),
    url(r'^hardware_save_xml_config', HardWareViews.save_xml_config),

    url(r'^to_xml_modal', XmlConfigViews.to_xml_modal),
    url(r'^xml_load_requirement', XmlConfigViews.load_requirement),
    url(r'^xml_save_ro_config', XmlConfigViews.save_ro_config),
    url(r'^xml_save_xml_config', XmlConfigViews.save_xml_config),
    url(r'^to_provider_modal', ProviderViews.to_provider_modal),
    url(r'^provider_load_requirement', ProviderViews.load_requirement),
    url(r'^provider_save_ro_config', ProviderViews.save_ro_config),
    url(r'^provider_save_xml_config', ProviderViews.save_xml_config),
    url(r'^do_check', MainViews.do_check),
    url(r'^ajax_query', FeatureViews.ajax_query),
    url(r'^check_dependence', FeatureViews.check_dependence),
    url(r'^check_resource_info', FeatureViews.check_resource_info),

    url(r'^to_jenkins_modal', JenkinsViews.to_jenkins_modal),
    url(r'^to_difference_modal', DifferenceViews.to_difference_modal),
    url(r'^generate_difference_pkg', DifferenceViews.generate_difference_pkg),

    url(r'^to_version_difference', VersionDifferenceView.show_version_difference),
    url(r'^select_difference', VersionDifferenceView.select_difference),
    url(r'^select_all_version', VersionDifferenceView.select_all_version),
    url(r'^select_by_version', VersionDifferenceView.select_by_version),
    url(r'^select_origin_difference', VersionDifferenceView.select_origin_difference),

    url(r'^to_workspace_modal', WorkspaceViews.to_workspace_modal),
    url(r'^load_all_app', WorkspaceViews.load_all_app),
    url(r'^load_workspace', WorkspaceViews.load_workspace),
    url(r'^load_folder', WorkspaceViews.load_folder),

    url(r'^get_require_init_value', FeatureViews.get_require_init_value),

    url(r'^source_order_name', VersionDifferenceView.getResourceOrderName),

    url(r'^to_version_info', views.to_version_info),
    url(r'^get_order_info_by_name', VersionDifferenceView.get_order_info_by_name),

    url(r'^get_launch_json', WorkspaceViews.get_launch_json),
    url(r'^load_apps', WorkspaceViews.load_apps),

    url(r'^to_show_visual_app', VisualAppViews.show_visual_app),
    url(r'^list_visual_app', VisualAppViews.list_visual_app),
    url(r'^to_visualapp_add', VisualAppViews.show_visual_add_app),
    url(r'^uniq_check_app', VisualAppViews.uniq_check_app),
    url(r'^add_save_app', VisualAppViews.add_save_app),
    url(r'^edit_save_app', VisualAppViews.edit_save_app),
    url(r'^to_visualapp_edit', VisualAppViews.show_visual_edit_app),
    url(r'^load_app_by_id', VisualAppViews.load_app_by_id),
    url(r'^viewImage', VisualAppViews.view_image),
    url(r'^visual_search_app', VisualAppViews.visual_search_app),

    url(r'^to_count_order', CountOrderViews.to_count_order),
    url(r'^count_order_info', CountOrderViews.count_order_info),
    url(r'^count_order_detail_info', CountOrderViews.count_order_detail_info),
    url(r'^count_publish_detail_info', CountOrderViews.count_publish_detail_info),
    url(r'^count_order_line', CountOrderViews.count_order_line),

]
