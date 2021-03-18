"""
    eZmax API Definition

    This API expose all the functionnalities for the eZmax and eZsign applications.  # noqa: E501

    The version of the OpenAPI document: 1.0.37
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
    from eZmaxinc/eZmax-SDK-python.model.field_pks_customer_code import FieldPksCustomerCode
    globals()['FieldPksCustomerCode'] = FieldPksCustomerCode


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
        ('e_webhook_module',): {
            'EZSIGN': "Ezsign",
            'MANAGEMENT': "Management",
        },
        ('e_webhook_ezsignevent',): {
            'DOCUMENTCOMPLETED': "DocumentCompleted",
            'FOLDERCOMPLETED': "FolderCompleted",
        },
        ('e_webhook_managementevent',): {
            'USERCREATED': "UserCreated",
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
            'pki_webhook_id': (int,),  # noqa: E501
            'e_webhook_module': (str,),  # noqa: E501
            'pks_customer_code': (FieldPksCustomerCode,),  # noqa: E501
            's_webhook_url': (str,),  # noqa: E501
            's_webhook_emailfailed': (str,),  # noqa: E501
            'e_webhook_ezsignevent': (str,),  # noqa: E501
            'e_webhook_managementevent': (str,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'pki_webhook_id': 'pkiWebhookID',  # noqa: E501
        'e_webhook_module': 'eWebhookModule',  # noqa: E501
        'pks_customer_code': 'pksCustomerCode',  # noqa: E501
        's_webhook_url': 'sWebhookUrl',  # noqa: E501
        's_webhook_emailfailed': 'sWebhookEmailfailed',  # noqa: E501
        'e_webhook_ezsignevent': 'eWebhookEzsignevent',  # noqa: E501
        'e_webhook_managementevent': 'eWebhookManagementevent',  # noqa: E501
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
    def __init__(self, pki_webhook_id, e_webhook_module, pks_customer_code, s_webhook_url, s_webhook_emailfailed, *args, **kwargs):  # noqa: E501
        """WebhookResponse - a model defined in OpenAPI

        Args:
            pki_webhook_id (int): The Webhook ID. This value is visible in the admin interface.
            e_webhook_module (str): The Module generating the Event.
            pks_customer_code (FieldPksCustomerCode):
            s_webhook_url (str): The url being called
            s_webhook_emailfailed (str): The email that will receive the webhook in case all attempts fail.

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
            e_webhook_ezsignevent (str): This Ezsign Event. This property will be set only if the Module is \"Ezsign\".. [optional]  # noqa: E501
            e_webhook_managementevent (str): This Management Event. This property will be set only if the Module is \"Management\".. [optional] if omitted the server will use the default value of "UserCreated"  # noqa: E501
        """

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

        self.pki_webhook_id = pki_webhook_id
        self.e_webhook_module = e_webhook_module
        self.pks_customer_code = pks_customer_code
        self.s_webhook_url = s_webhook_url
        self.s_webhook_emailfailed = s_webhook_emailfailed
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
