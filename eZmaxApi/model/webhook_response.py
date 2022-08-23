"""
    eZmax API Definition (Full)

    This API expose all the functionnalities for the eZmax and eZsign applications.  # noqa: E501

    The version of the OpenAPI document: 1.1.10
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
    from eZmaxApi.model.field_e_webhook_ezsignevent import FieldEWebhookEzsignevent
    from eZmaxApi.model.field_e_webhook_managementevent import FieldEWebhookManagementevent
    from eZmaxApi.model.field_e_webhook_module import FieldEWebhookModule
    from eZmaxApi.model.field_pki_ezsignfoldertype_id import FieldPkiEzsignfoldertypeID
    globals()['FieldEWebhookEzsignevent'] = FieldEWebhookEzsignevent
    globals()['FieldEWebhookManagementevent'] = FieldEWebhookManagementevent
    globals()['FieldEWebhookModule'] = FieldEWebhookModule
    globals()['FieldPkiEzsignfoldertypeID'] = FieldPkiEzsignfoldertypeID


class WebhookResponse(ModelNormal):
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
            'pki_webhook_id': (int,),  # noqa: E501
            's_webhook_description': (str,),  # noqa: E501
            'e_webhook_module': (FieldEWebhookModule,),  # noqa: E501
            's_webhook_url': (str,),  # noqa: E501
            's_webhook_emailfailed': (str,),  # noqa: E501
            'b_webhook_skipsslvalidation': (bool,),  # noqa: E501
            'fki_ezsignfoldertype_id': (FieldPkiEzsignfoldertypeID,),  # noqa: E501
            's_ezsignfoldertype_name_x': (str,),  # noqa: E501
            'e_webhook_ezsignevent': (FieldEWebhookEzsignevent,),  # noqa: E501
            'e_webhook_managementevent': (FieldEWebhookManagementevent,),  # noqa: E501
            'b_webhook_isactive': (bool,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'pki_webhook_id': 'pkiWebhookID',  # noqa: E501
        's_webhook_description': 'sWebhookDescription',  # noqa: E501
        'e_webhook_module': 'eWebhookModule',  # noqa: E501
        's_webhook_url': 'sWebhookUrl',  # noqa: E501
        's_webhook_emailfailed': 'sWebhookEmailfailed',  # noqa: E501
        'b_webhook_skipsslvalidation': 'bWebhookSkipsslvalidation',  # noqa: E501
        'fki_ezsignfoldertype_id': 'fkiEzsignfoldertypeID',  # noqa: E501
        's_ezsignfoldertype_name_x': 'sEzsignfoldertypeNameX',  # noqa: E501
        'e_webhook_ezsignevent': 'eWebhookEzsignevent',  # noqa: E501
        'e_webhook_managementevent': 'eWebhookManagementevent',  # noqa: E501
        'b_webhook_isactive': 'bWebhookIsactive',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, pki_webhook_id, s_webhook_description, e_webhook_module, s_webhook_url, s_webhook_emailfailed, b_webhook_skipsslvalidation, *args, **kwargs):  # noqa: E501
        """WebhookResponse - a model defined in OpenAPI

        Args:
            pki_webhook_id (int): The unique ID of the Webhook
            s_webhook_description (str): The description of the Webhook
            e_webhook_module (FieldEWebhookModule):
            s_webhook_url (str): The URL of the Webhook callback
            s_webhook_emailfailed (str): The email that will receive the Webhook in case all attempts fail
            b_webhook_skipsslvalidation (bool): Wheter the server's SSL certificate should be validated or not. Not recommended to skip for production use

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
            fki_ezsignfoldertype_id (FieldPkiEzsignfoldertypeID): [optional]  # noqa: E501
            s_ezsignfoldertype_name_x (str): The name of the Ezsignfoldertype in the language of the requester. [optional]  # noqa: E501
            e_webhook_ezsignevent (FieldEWebhookEzsignevent): [optional]  # noqa: E501
            e_webhook_managementevent (FieldEWebhookManagementevent): [optional]  # noqa: E501
            b_webhook_isactive (bool): Whether the Webhook is active or not. [optional]  # noqa: E501
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

        self.pki_webhook_id = pki_webhook_id
        self.s_webhook_description = s_webhook_description
        self.e_webhook_module = e_webhook_module
        self.s_webhook_url = s_webhook_url
        self.s_webhook_emailfailed = s_webhook_emailfailed
        self.b_webhook_skipsslvalidation = b_webhook_skipsslvalidation
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
    def __init__(self, pki_webhook_id, s_webhook_description, e_webhook_module, s_webhook_url, s_webhook_emailfailed, b_webhook_skipsslvalidation, *args, **kwargs):  # noqa: E501
        """WebhookResponse - a model defined in OpenAPI

        Args:
            pki_webhook_id (int): The unique ID of the Webhook
            s_webhook_description (str): The description of the Webhook
            e_webhook_module (FieldEWebhookModule):
            s_webhook_url (str): The URL of the Webhook callback
            s_webhook_emailfailed (str): The email that will receive the Webhook in case all attempts fail
            b_webhook_skipsslvalidation (bool): Wheter the server's SSL certificate should be validated or not. Not recommended to skip for production use

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
            fki_ezsignfoldertype_id (FieldPkiEzsignfoldertypeID): [optional]  # noqa: E501
            s_ezsignfoldertype_name_x (str): The name of the Ezsignfoldertype in the language of the requester. [optional]  # noqa: E501
            e_webhook_ezsignevent (FieldEWebhookEzsignevent): [optional]  # noqa: E501
            e_webhook_managementevent (FieldEWebhookManagementevent): [optional]  # noqa: E501
            b_webhook_isactive (bool): Whether the Webhook is active or not. [optional]  # noqa: E501
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

        self.pki_webhook_id = pki_webhook_id
        self.s_webhook_description = s_webhook_description
        self.e_webhook_module = e_webhook_module
        self.s_webhook_url = s_webhook_url
        self.s_webhook_emailfailed = s_webhook_emailfailed
        self.b_webhook_skipsslvalidation = b_webhook_skipsslvalidation
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
