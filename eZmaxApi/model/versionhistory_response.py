"""
    eZmax API Definition (Full)

    This API expose all the functionnalities for the eZmax and eZsign applications.  # noqa: E501

    The version of the OpenAPI document: 1.1.16
    Contact: support-api@ezmax.ca
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from eZmaxApi.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
    OpenApiModel
)
from eZmaxApi.exceptions import ApiAttributeError


def lazy_import():
    from eZmaxApi.model.field_e_versionhistory_type import FieldEVersionhistoryType
    from eZmaxApi.model.field_e_versionhistory_usertype import FieldEVersionhistoryUsertype
    from eZmaxApi.model.field_pki_module_id import FieldPkiModuleID
    from eZmaxApi.model.field_pki_modulesection_id import FieldPkiModulesectionID
    from eZmaxApi.model.field_pki_versionhistory_id import FieldPkiVersionhistoryID
    from eZmaxApi.model.multilingual_versionhistory_detail import MultilingualVersionhistoryDetail
    globals()['FieldEVersionhistoryType'] = FieldEVersionhistoryType
    globals()['FieldEVersionhistoryUsertype'] = FieldEVersionhistoryUsertype
    globals()['FieldPkiModuleID'] = FieldPkiModuleID
    globals()['FieldPkiModulesectionID'] = FieldPkiModulesectionID
    globals()['FieldPkiVersionhistoryID'] = FieldPkiVersionhistoryID
    globals()['MultilingualVersionhistoryDetail'] = MultilingualVersionhistoryDetail


class VersionhistoryResponse(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        lazy_import()
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'pki_versionhistory_id': (FieldPkiVersionhistoryID,),  # noqa: E501
            'obj_versionhistory_detail': (MultilingualVersionhistoryDetail,),  # noqa: E501
            'dt_versionhistory_date': (str,),  # noqa: E501
            'e_versionhistory_type': (FieldEVersionhistoryType,),  # noqa: E501
            'b_versionhistory_draft': (bool,),  # noqa: E501
            'fki_module_id': (FieldPkiModuleID,),  # noqa: E501
            'fki_modulesection_id': (FieldPkiModulesectionID,),  # noqa: E501
            's_module_name_x': (str,),  # noqa: E501
            's_modulesection_name_x': (str,),  # noqa: E501
            'e_versionhistory_usertype': (FieldEVersionhistoryUsertype,),  # noqa: E501
            'dt_versionhistory_dateend': (str,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'pki_versionhistory_id': 'pkiVersionhistoryID',  # noqa: E501
        'obj_versionhistory_detail': 'objVersionhistoryDetail',  # noqa: E501
        'dt_versionhistory_date': 'dtVersionhistoryDate',  # noqa: E501
        'e_versionhistory_type': 'eVersionhistoryType',  # noqa: E501
        'b_versionhistory_draft': 'bVersionhistoryDraft',  # noqa: E501
        'fki_module_id': 'fkiModuleID',  # noqa: E501
        'fki_modulesection_id': 'fkiModulesectionID',  # noqa: E501
        's_module_name_x': 'sModuleNameX',  # noqa: E501
        's_modulesection_name_x': 'sModulesectionNameX',  # noqa: E501
        'e_versionhistory_usertype': 'eVersionhistoryUsertype',  # noqa: E501
        'dt_versionhistory_dateend': 'dtVersionhistoryDateend',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, pki_versionhistory_id, obj_versionhistory_detail, dt_versionhistory_date, e_versionhistory_type, b_versionhistory_draft, *args, **kwargs):  # noqa: E501
        """VersionhistoryResponse - a model defined in OpenAPI

        Args:
            pki_versionhistory_id (FieldPkiVersionhistoryID):
            obj_versionhistory_detail (MultilingualVersionhistoryDetail):
            dt_versionhistory_date (str): The date  at which the Versionhistory was published or should be published
            e_versionhistory_type (FieldEVersionhistoryType):
            b_versionhistory_draft (bool): Whether the Versionhistory is published or still a draft

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            fki_module_id (FieldPkiModuleID): [optional]  # noqa: E501
            fki_modulesection_id (FieldPkiModulesectionID): [optional]  # noqa: E501
            s_module_name_x (str): The Name of the Module in the language of the requester. [optional]  # noqa: E501
            s_modulesection_name_x (str): The Name of the Modulesection in the language of the requester. [optional]  # noqa: E501
            e_versionhistory_usertype (FieldEVersionhistoryUsertype): [optional]  # noqa: E501
            dt_versionhistory_dateend (str): The date  at which the Versionhistory will no longer be visible. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', True)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                            args,
                            self.__class__.__name__,
                        ),
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.pki_versionhistory_id = pki_versionhistory_id
        self.obj_versionhistory_detail = obj_versionhistory_detail
        self.dt_versionhistory_date = dt_versionhistory_date
        self.e_versionhistory_type = e_versionhistory_type
        self.b_versionhistory_draft = b_versionhistory_draft
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, pki_versionhistory_id, obj_versionhistory_detail, dt_versionhistory_date, e_versionhistory_type, b_versionhistory_draft, *args, **kwargs):  # noqa: E501
        """VersionhistoryResponse - a model defined in OpenAPI

        Args:
            pki_versionhistory_id (FieldPkiVersionhistoryID):
            obj_versionhistory_detail (MultilingualVersionhistoryDetail):
            dt_versionhistory_date (str): The date  at which the Versionhistory was published or should be published
            e_versionhistory_type (FieldEVersionhistoryType):
            b_versionhistory_draft (bool): Whether the Versionhistory is published or still a draft

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            fki_module_id (FieldPkiModuleID): [optional]  # noqa: E501
            fki_modulesection_id (FieldPkiModulesectionID): [optional]  # noqa: E501
            s_module_name_x (str): The Name of the Module in the language of the requester. [optional]  # noqa: E501
            s_modulesection_name_x (str): The Name of the Modulesection in the language of the requester. [optional]  # noqa: E501
            e_versionhistory_usertype (FieldEVersionhistoryUsertype): [optional]  # noqa: E501
            dt_versionhistory_dateend (str): The date  at which the Versionhistory will no longer be visible. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                            args,
                            self.__class__.__name__,
                        ),
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.pki_versionhistory_id = pki_versionhistory_id
        self.obj_versionhistory_detail = obj_versionhistory_detail
        self.dt_versionhistory_date = dt_versionhistory_date
        self.e_versionhistory_type = e_versionhistory_type
        self.b_versionhistory_draft = b_versionhistory_draft
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")
