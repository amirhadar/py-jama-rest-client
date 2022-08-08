from typing import Dict


class JamaQueryTestCaseParamValueConstatns:
    AUTOMATION_FRAMEWORK = 'data.fields.automation_framework$143'
    REQUIRED_REGIONS = 'data.fields.required_regions$143'
    PRE_REQUIREMENTS = 'data.fields.prerequirements$143'
    POST_REQUIREMENTS = 'data.fields.post_requirements$143'
    SCANNER_TYPE = 'data.fields.system$143'


class JamaQueryParamNameConstants:
    ITEMS_PER_PAGE = 'maxResults'
    OFFSET = 'startAt'
    PROJECT_ID = 'project'
    CONTAINS = 'contains'
    INCLUDE = 'include'
    DATA = 'data'
    LINKED = 'linked'


class JamaLabelExpressionConstant:
    TEST_CASE_TAG = 'testCaseTag'
    EXCLUSIVE_TAG = 'exclusive'
    EXCLUSIVE_TAG_VALUE = 'exclusive_test'


class JamaParams:
    @staticmethod
    def get_project_query_param(project_id: int) -> Dict[str, int]:
        return {JamaQueryParamNameConstants.PROJECT_ID: project_id}

    @staticmethod
    def get_jama_linked_data_params():
        return {
            JamaQueryParamNameConstants.INCLUDE: [
                JamaQueryTestCaseParamValueConstatns.AUTOMATION_FRAMEWORK,
                JamaQueryTestCaseParamValueConstatns.REQUIRED_REGIONS,
                JamaQueryTestCaseParamValueConstatns.PRE_REQUIREMENTS,
                JamaQueryTestCaseParamValueConstatns.POST_REQUIREMENTS,
                JamaQueryTestCaseParamValueConstatns.SCANNER_TYPE,
            ]
        }
