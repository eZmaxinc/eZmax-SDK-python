"""
    eZmax API Definition

    This API expose all the functionnalities for the eZmax and eZsign applications.  # noqa: E501

    The version of the OpenAPI document: 1.0.46
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
)
from ..model_utils import OpenApiModel
from eZmaxApi.exceptions import ApiAttributeError


def lazy_import():
    from eZmaxApi.model.common_audit import CommonAudit
    from eZmaxApi.model.ezsigndocument_response import EzsigndocumentResponse
    from eZmaxApi.model.field_e_ezsigndocument_step import FieldEEzsigndocumentStep
    from eZmaxApi.model.field_pki_language_id import FieldPkiLanguageID
    globals()['CommonAudit'] = CommonAudit
    globals()['EzsigndocumentResponse'] = EzsigndocumentResponse
    globals()['FieldEEzsigndocumentStep'] = FieldEEzsigndocumentStep
    globals()['FieldPkiLanguageID'] = FieldPkiLanguageID


class EzsigndocumentResponseCompound(ModelComposed):
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
            'fki_ezsignfolder_id': (int,),  # noqa: E501
            'dt_ezsigndocument_duedate': (str,),  # noqa: E501
            'fki_language_id': (FieldPkiLanguageID,),  # noqa: E501
            's_ezsigndocument_name': (str,),  # noqa: E501
            'pki_ezsigndocument_id': (int,),  # noqa: E501
            'e_ezsigndocument_step': (FieldEEzsigndocumentStep,),  # noqa: E501
            'dt_ezsigndocument_firstsend': (str,),  # noqa: E501
            'dt_ezsigndocument_lastsend': (str,),  # noqa: E501
            'i_ezsigndocument_order': (int,),  # noqa: E501
            'i_ezsigndocument_pagetotal': (int,),  # noqa: E501
            'i_ezsigndocument_signaturesigned': (int,),  # noqa: E501
            'i_ezsigndocument_signaturetotal': (int,),  # noqa: E501
            's_ezsigndocument_md5initial': (str,),  # noqa: E501
            's_ezsigndocument_md5signed': (str,),  # noqa: E501
            'obj_audit': (CommonAudit,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'fki_ezsignfolder_id': 'fkiEzsignfolderID',  # noqa: E501
        'dt_ezsigndocument_duedate': 'dtEzsigndocumentDuedate',  # noqa: E501
        'fki_language_id': 'fkiLanguageID',  # noqa: E501
        's_ezsigndocument_name': 'sEzsigndocumentName',  # noqa: E501
        'pki_ezsigndocument_id': 'pkiEzsigndocumentID',  # noqa: E501
        'e_ezsigndocument_step': 'eEzsigndocumentStep',  # noqa: E501
        'dt_ezsigndocument_firstsend': 'dtEzsigndocumentFirstsend',  # noqa: E501
        'dt_ezsigndocument_lastsend': 'dtEzsigndocumentLastsend',  # noqa: E501
        'i_ezsigndocument_order': 'iEzsigndocumentOrder',  # noqa: E501
        'i_ezsigndocument_pagetotal': 'iEzsigndocumentPagetotal',  # noqa: E501
        'i_ezsigndocument_signaturesigned': 'iEzsigndocumentSignaturesigned',  # noqa: E501
        'i_ezsigndocument_signaturetotal': 'iEzsigndocumentSignaturetotal',  # noqa: E501
        's_ezsigndocument_md5initial': 'sEzsigndocumentMD5initial',  # noqa: E501
        's_ezsigndocument_md5signed': 'sEzsigndocumentMD5signed',  # noqa: E501
        'obj_audit': 'objAudit',  # noqa: E501
    }

    read_only_vars = {
    }

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """EzsigndocumentResponseCompound - a model defined in OpenAPI

        Keyword Args:
            fki_ezsignfolder_id (int): The unique ID of the Ezsignfolder
            dt_ezsigndocument_duedate (str): The maximum date and time at which the document can be signed.
            fki_language_id (FieldPkiLanguageID):
            s_ezsigndocument_name (str): The name of the document that will be presented to Ezsignfoldersignerassociations
            pki_ezsigndocument_id (int): The unique ID of the Ezsigntemplate
            e_ezsigndocument_step (FieldEEzsigndocumentStep):
            dt_ezsigndocument_firstsend (str): The date and time when the Ezsigndocument was first sent.
            dt_ezsigndocument_lastsend (str): The date and time when the Ezsigndocument was sent the last time.
            i_ezsigndocument_order (int): The order in which the Ezsigndocument will be presented to the signatory in the Ezsignfolder.
            i_ezsigndocument_pagetotal (int): The number of pages in the Ezsigndocument.
            i_ezsigndocument_signaturesigned (int): The number of signatures that were signed in the document.
            i_ezsigndocument_signaturetotal (int): The number of total signatures that were requested in the Ezsigndocument.
            s_ezsigndocument_md5initial (str): MD5 Hash of the initial PDF Document before signatures were applied to it.
            s_ezsigndocument_md5signed (str): MD5 Hash of the final PDF Document after all signatures were applied to it.
            obj_audit (CommonAudit):
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

        self = super(OpenApiModel, cls).__new__(cls)

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

        constant_args = {
            '_check_type': _check_type,
            '_path_to_item': _path_to_item,
            '_spec_property_naming': _spec_property_naming,
            '_configuration': _configuration,
            '_visited_composed_classes': self._visited_composed_classes,
        }
        composed_info = validate_get_composed_info(
            constant_args, kwargs, self)
        self._composed_instances = composed_info[0]
        self._var_name_to_model_instances = composed_info[1]
        self._additional_properties_model_instances = composed_info[2]
        discarded_args = composed_info[3]

        for var_name, var_value in kwargs.items():
            if var_name in discarded_args and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self._additional_properties_model_instances:
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
        '_composed_instances',
        '_var_name_to_model_instances',
        '_additional_properties_model_instances',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """EzsigndocumentResponseCompound - a model defined in OpenAPI

        Keyword Args:
            fki_ezsignfolder_id (int): The unique ID of the Ezsignfolder
            dt_ezsigndocument_duedate (str): The maximum date and time at which the document can be signed.
            fki_language_id (FieldPkiLanguageID):
            s_ezsigndocument_name (str): The name of the document that will be presented to Ezsignfoldersignerassociations
            pki_ezsigndocument_id (int): The unique ID of the Ezsigntemplate
            e_ezsigndocument_step (FieldEEzsigndocumentStep):
            dt_ezsigndocument_firstsend (str): The date and time when the Ezsigndocument was first sent.
            dt_ezsigndocument_lastsend (str): The date and time when the Ezsigndocument was sent the last time.
            i_ezsigndocument_order (int): The order in which the Ezsigndocument will be presented to the signatory in the Ezsignfolder.
            i_ezsigndocument_pagetotal (int): The number of pages in the Ezsigndocument.
            i_ezsigndocument_signaturesigned (int): The number of signatures that were signed in the document.
            i_ezsigndocument_signaturetotal (int): The number of total signatures that were requested in the Ezsigndocument.
            s_ezsigndocument_md5initial (str): MD5 Hash of the initial PDF Document before signatures were applied to it.
            s_ezsigndocument_md5signed (str): MD5 Hash of the final PDF Document after all signatures were applied to it.
            obj_audit (CommonAudit):
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

        constant_args = {
            '_check_type': _check_type,
            '_path_to_item': _path_to_item,
            '_spec_property_naming': _spec_property_naming,
            '_configuration': _configuration,
            '_visited_composed_classes': self._visited_composed_classes,
        }
        composed_info = validate_get_composed_info(
            constant_args, kwargs, self)
        self._composed_instances = composed_info[0]
        self._var_name_to_model_instances = composed_info[1]
        self._additional_properties_model_instances = composed_info[2]
        discarded_args = composed_info[3]

        for var_name, var_value in kwargs.items():
            if var_name in discarded_args and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self._additional_properties_model_instances:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")

    @cached_property
    def _composed_schemas():
        # we need this here to make our import statements work
        # we must store _composed_schemas in here so the code is only run
        # when we invoke this method. If we kept this at the class
        # level we would get an error beause the class level
        # code would be run when this module is imported, and these composed
        # classes don't exist yet because their module has not finished
        # loading
        lazy_import()
        return {
          'anyOf': [
          ],
          'allOf': [
              EzsigndocumentResponse,
          ],
          'oneOf': [
          ],
        }
