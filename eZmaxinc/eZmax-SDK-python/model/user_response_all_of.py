"""
    eZmax API Definition

    This API expose all the functionnalities for the eZmax and eZsign application.  We provide SDKs for customers. They are generated using OpenAPI codegen, we encourage customers to use them as we also provide samples for them.  You can choose to build your own implementation manually or can use any compatible OpenAPI 3.0 generator like Swagger Codegen, OpenAPI codegen or any commercial generators.  If you need helping understanding how to use this API, don't waste too much time looking for it. Contact support-api@ezmax.ca, we're here to help. We are developpers so we know programmers don't like bad documentation. If you don't find what you need in the documentation, let us know, we'll improve it and put you rapidly up on track.  # noqa: E501

    The version of the OpenAPI document: 1.0.28
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
    from eZmaxinc/eZmax-SDK-python.model.common_audit import CommonAudit
    from eZmaxinc/eZmax-SDK-python.model.field_e_user_type import FieldEUserType
    from eZmaxinc/eZmax-SDK-python.model.field_pki_language_id import FieldPkiLanguageID
    globals()['CommonAudit'] = CommonAudit
    globals()['FieldEUserType'] = FieldEUserType
    globals()['FieldPkiLanguageID'] = FieldPkiLanguageID


class UserResponseAllOf(ModelNormal):
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
            'pki_user_id': (int,),  # noqa: E501
            'fki_language_id': (FieldPkiLanguageID,),  # noqa: E501
            'e_user_type': (FieldEUserType,),  # noqa: E501
            's_user_firstname': (str,),  # noqa: E501
            's_user_lastname': (str,),  # noqa: E501
            's_user_loginname': (str,),  # noqa: E501
            'obj_audit': (CommonAudit,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'pki_user_id': 'pkiUserID',  # noqa: E501
        'fki_language_id': 'fkiLanguageID',  # noqa: E501
        'e_user_type': 'eUserType',  # noqa: E501
        's_user_firstname': 'sUserFirstname',  # noqa: E501
        's_user_lastname': 'sUserLastname',  # noqa: E501
        's_user_loginname': 'sUserLoginname',  # noqa: E501
        'obj_audit': 'objAudit',  # noqa: E501
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
    def __init__(self, pki_user_id, fki_language_id, e_user_type, s_user_firstname, s_user_lastname, s_user_loginname, obj_audit, *args, **kwargs):  # noqa: E501
        """UserResponseAllOf - a model defined in OpenAPI

        Args:
            pki_user_id (int): The unique ID of the User
            fki_language_id (FieldPkiLanguageID):
            e_user_type (FieldEUserType):
            s_user_firstname (str): The First name of the user
            s_user_lastname (str): The Last name of the user
            s_user_loginname (str): The Login name of the User.
            obj_audit (CommonAudit):

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

        self.pki_user_id = pki_user_id
        self.fki_language_id = fki_language_id
        self.e_user_type = e_user_type
        self.s_user_firstname = s_user_firstname
        self.s_user_lastname = s_user_lastname
        self.s_user_loginname = s_user_loginname
        self.obj_audit = obj_audit
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)