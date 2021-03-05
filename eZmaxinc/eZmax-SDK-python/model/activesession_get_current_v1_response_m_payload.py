"""
    eZmax API Definition

    This API expose all the functionnalities for the eZmax and eZsign applications.  # noqa: E501

    The version of the OpenAPI document: 1.0.32
    Contact: support-api@ezmax.ca
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from eZmaxinc/eZmax-SDK-python.model_utils import (  # noqa: F401
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
)

def lazy_import():
    from eZmaxinc/eZmax-SDK-python.model.field_pki_language_id import FieldPkiLanguageID
    globals()['FieldPkiLanguageID'] = FieldPkiLanguageID


class ActivesessionGetCurrentV1ResponseMPayload(ModelNormal):
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
        ('e_activesession_sessiontype',): {
            'NORMAL': "Normal",
        },
    }

    validations = {
    }

    additional_properties_type = None

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
            's_customer_code': (str,),  # noqa: E501
            'e_activesession_sessiontype': (str,),  # noqa: E501
            'fki_language_id': (FieldPkiLanguageID,),  # noqa: E501
            's_company_name_x': (str,),  # noqa: E501
            's_department_name_x': (str,),  # noqa: E501
            'a_registered_modules': ([str],),  # noqa: E501
            'a_permissions': ([int],),  # noqa: E501
            'fki_user_id': (int,),  # noqa: E501
            'fki_apikey_id': (int,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        's_customer_code': 'sCustomerCode',  # noqa: E501
        'e_activesession_sessiontype': 'eActivesessionSessiontype',  # noqa: E501
        'fki_language_id': 'fkiLanguageID',  # noqa: E501
        's_company_name_x': 'sCompanyNameX',  # noqa: E501
        's_department_name_x': 'sDepartmentNameX',  # noqa: E501
        'a_registered_modules': 'a_RegisteredModules',  # noqa: E501
        'a_permissions': 'a_Permissions',  # noqa: E501
        'fki_user_id': 'fkiUserID',  # noqa: E501
        'fki_apikey_id': 'fkiApikeyID',  # noqa: E501
    }

    _composed_schemas = {}

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, s_customer_code, fki_language_id, s_company_name_x, s_department_name_x, a_registered_modules, a_permissions, fki_user_id, fki_apikey_id, *args, **kwargs):  # noqa: E501
        """ActivesessionGetCurrentV1ResponseMPayload - a model defined in OpenAPI

        Args:
            s_customer_code (str): The customer code specific to the client in which the API request is being made
            fki_language_id (FieldPkiLanguageID):
            s_company_name_x (str): The name of the active Company in the current language
            s_department_name_x (str): The name of the active Department in the current language
            a_registered_modules ([str]): An Array of Registered modules.  These are the modules that are Licensed to be used by the User or the API Key.
            a_permissions ([int]): An array of permissions granted to the user or api key
            fki_user_id (int): The unique ID of the User
            fki_apikey_id (int): The unique ID of the Apikey

        Keyword Args:
            e_activesession_sessiontype (str): The type of session used for the API request call. defaults to "Normal", must be one of ["Normal", ]  # noqa: E501
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
        """

        e_activesession_sessiontype = kwargs.get('e_activesession_sessiontype', "Normal")
        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
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

        self.s_customer_code = s_customer_code
        self.e_activesession_sessiontype = e_activesession_sessiontype
        self.fki_language_id = fki_language_id
        self.s_company_name_x = s_company_name_x
        self.s_department_name_x = s_department_name_x
        self.a_registered_modules = a_registered_modules
        self.a_permissions = a_permissions
        self.fki_user_id = fki_user_id
        self.fki_apikey_id = fki_apikey_id
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
