"""
    eZmax API Definition (Full)

    This API expose all the functionnalities for the eZmax and eZsign applications.  # noqa: E501

    The version of the OpenAPI document: 1.1.14
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
    from eZmaxApi.model.ezsigntemplatesignature_response_compound import EzsigntemplatesignatureResponseCompound
    from eZmaxApi.model.ezsigntemplatesignaturecustomdate_response_compound import EzsigntemplatesignaturecustomdateResponseCompound
    from eZmaxApi.model.field_e_ezsigntemplatesignature_attachmentnamesource import FieldEEzsigntemplatesignatureAttachmentnamesource
    from eZmaxApi.model.field_e_ezsigntemplatesignature_font import FieldEEzsigntemplatesignatureFont
    from eZmaxApi.model.field_e_ezsigntemplatesignature_tooltipposition import FieldEEzsigntemplatesignatureTooltipposition
    from eZmaxApi.model.field_e_ezsigntemplatesignature_type import FieldEEzsigntemplatesignatureType
    from eZmaxApi.model.field_i_ezsigntemplatedocumentpage_pagenumber import FieldIEzsigntemplatedocumentpagePagenumber
    from eZmaxApi.model.field_i_ezsigntemplatesignature_step import FieldIEzsigntemplatesignatureStep
    from eZmaxApi.model.field_i_ezsigntemplatesignature_x import FieldIEzsigntemplatesignatureX
    from eZmaxApi.model.field_i_ezsigntemplatesignature_y import FieldIEzsigntemplatesignatureY
    from eZmaxApi.model.field_pki_ezsigntemplatedocument_id import FieldPkiEzsigntemplatedocumentID
    from eZmaxApi.model.field_pki_ezsigntemplatesignature_id import FieldPkiEzsigntemplatesignatureID
    from eZmaxApi.model.field_pki_ezsigntemplatesigner_id import FieldPkiEzsigntemplatesignerID
    globals()['EzsigntemplatesignatureResponseCompound'] = EzsigntemplatesignatureResponseCompound
    globals()['EzsigntemplatesignaturecustomdateResponseCompound'] = EzsigntemplatesignaturecustomdateResponseCompound
    globals()['FieldEEzsigntemplatesignatureAttachmentnamesource'] = FieldEEzsigntemplatesignatureAttachmentnamesource
    globals()['FieldEEzsigntemplatesignatureFont'] = FieldEEzsigntemplatesignatureFont
    globals()['FieldEEzsigntemplatesignatureTooltipposition'] = FieldEEzsigntemplatesignatureTooltipposition
    globals()['FieldEEzsigntemplatesignatureType'] = FieldEEzsigntemplatesignatureType
    globals()['FieldIEzsigntemplatedocumentpagePagenumber'] = FieldIEzsigntemplatedocumentpagePagenumber
    globals()['FieldIEzsigntemplatesignatureStep'] = FieldIEzsigntemplatesignatureStep
    globals()['FieldIEzsigntemplatesignatureX'] = FieldIEzsigntemplatesignatureX
    globals()['FieldIEzsigntemplatesignatureY'] = FieldIEzsigntemplatesignatureY
    globals()['FieldPkiEzsigntemplatedocumentID'] = FieldPkiEzsigntemplatedocumentID
    globals()['FieldPkiEzsigntemplatesignatureID'] = FieldPkiEzsigntemplatesignatureID
    globals()['FieldPkiEzsigntemplatesignerID'] = FieldPkiEzsigntemplatesignerID


class EzsigntemplatesignatureGetObjectV1ResponseMPayload(ModelComposed):
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
            'pki_ezsigntemplatesignature_id': (FieldPkiEzsigntemplatesignatureID,),  # noqa: E501
            'fki_ezsigntemplatedocument_id': (FieldPkiEzsigntemplatedocumentID,),  # noqa: E501
            'fki_ezsigntemplatesigner_id': (FieldPkiEzsigntemplatesignerID,),  # noqa: E501
            'i_ezsigntemplatedocumentpage_pagenumber': (FieldIEzsigntemplatedocumentpagePagenumber,),  # noqa: E501
            'i_ezsigntemplatesignature_x': (FieldIEzsigntemplatesignatureX,),  # noqa: E501
            'i_ezsigntemplatesignature_y': (FieldIEzsigntemplatesignatureY,),  # noqa: E501
            'i_ezsigntemplatesignature_step': (FieldIEzsigntemplatesignatureStep,),  # noqa: E501
            'e_ezsigntemplatesignature_type': (FieldEEzsigntemplatesignatureType,),  # noqa: E501
            'fki_ezsigntemplatesigner_id_validation': (FieldPkiEzsigntemplatesignerID,),  # noqa: E501
            't_ezsigntemplatesignature_tooltip': (str,),  # noqa: E501
            'e_ezsigntemplatesignature_tooltipposition': (FieldEEzsigntemplatesignatureTooltipposition,),  # noqa: E501
            'e_ezsigntemplatesignature_font': (FieldEEzsigntemplatesignatureFont,),  # noqa: E501
            'i_ezsigntemplatesignature_validationstep': (int,),  # noqa: E501
            's_ezsigntemplatesignature_attachmentdescription': (str,),  # noqa: E501
            'e_ezsigntemplatesignature_attachmentnamesource': (FieldEEzsigntemplatesignatureAttachmentnamesource,),  # noqa: E501
            'b_ezsigntemplatesignature_required': (bool,),  # noqa: E501
            'b_ezsigntemplatesignature_customdate': (bool,),  # noqa: E501
            'a_obj_ezsigntemplatesignaturecustomdate': ([EzsigntemplatesignaturecustomdateResponseCompound],),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'pki_ezsigntemplatesignature_id': 'pkiEzsigntemplatesignatureID',  # noqa: E501
        'fki_ezsigntemplatedocument_id': 'fkiEzsigntemplatedocumentID',  # noqa: E501
        'fki_ezsigntemplatesigner_id': 'fkiEzsigntemplatesignerID',  # noqa: E501
        'i_ezsigntemplatedocumentpage_pagenumber': 'iEzsigntemplatedocumentpagePagenumber',  # noqa: E501
        'i_ezsigntemplatesignature_x': 'iEzsigntemplatesignatureX',  # noqa: E501
        'i_ezsigntemplatesignature_y': 'iEzsigntemplatesignatureY',  # noqa: E501
        'i_ezsigntemplatesignature_step': 'iEzsigntemplatesignatureStep',  # noqa: E501
        'e_ezsigntemplatesignature_type': 'eEzsigntemplatesignatureType',  # noqa: E501
        'fki_ezsigntemplatesigner_id_validation': 'fkiEzsigntemplatesignerIDValidation',  # noqa: E501
        't_ezsigntemplatesignature_tooltip': 'tEzsigntemplatesignatureTooltip',  # noqa: E501
        'e_ezsigntemplatesignature_tooltipposition': 'eEzsigntemplatesignatureTooltipposition',  # noqa: E501
        'e_ezsigntemplatesignature_font': 'eEzsigntemplatesignatureFont',  # noqa: E501
        'i_ezsigntemplatesignature_validationstep': 'iEzsigntemplatesignatureValidationstep',  # noqa: E501
        's_ezsigntemplatesignature_attachmentdescription': 'sEzsigntemplatesignatureAttachmentdescription',  # noqa: E501
        'e_ezsigntemplatesignature_attachmentnamesource': 'eEzsigntemplatesignatureAttachmentnamesource',  # noqa: E501
        'b_ezsigntemplatesignature_required': 'bEzsigntemplatesignatureRequired',  # noqa: E501
        'b_ezsigntemplatesignature_customdate': 'bEzsigntemplatesignatureCustomdate',  # noqa: E501
        'a_obj_ezsigntemplatesignaturecustomdate': 'a_objEzsigntemplatesignaturecustomdate',  # noqa: E501
    }

    read_only_vars = {
    }

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """EzsigntemplatesignatureGetObjectV1ResponseMPayload - a model defined in OpenAPI

        Keyword Args:
            pki_ezsigntemplatesignature_id (FieldPkiEzsigntemplatesignatureID):
            fki_ezsigntemplatedocument_id (FieldPkiEzsigntemplatedocumentID):
            fki_ezsigntemplatesigner_id (FieldPkiEzsigntemplatesignerID):
            i_ezsigntemplatedocumentpage_pagenumber (FieldIEzsigntemplatedocumentpagePagenumber):
            i_ezsigntemplatesignature_x (FieldIEzsigntemplatesignatureX):
            i_ezsigntemplatesignature_y (FieldIEzsigntemplatesignatureY):
            i_ezsigntemplatesignature_step (FieldIEzsigntemplatesignatureStep):
            e_ezsigntemplatesignature_type (FieldEEzsigntemplatesignatureType):
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
            fki_ezsigntemplatesigner_id_validation (FieldPkiEzsigntemplatesignerID): [optional]  # noqa: E501
            t_ezsigntemplatesignature_tooltip (str): A tooltip that will be presented to Ezsigntemplatesigner about the Ezsigntemplatesignature. [optional]  # noqa: E501
            e_ezsigntemplatesignature_tooltipposition (FieldEEzsigntemplatesignatureTooltipposition): [optional]  # noqa: E501
            e_ezsigntemplatesignature_font (FieldEEzsigntemplatesignatureFont): [optional]  # noqa: E501
            i_ezsigntemplatesignature_validationstep (int): The step when the Ezsigntemplatesigner will be invited to validate the Ezsigntemplatesignature of eEzsigntemplatesignatureType Attachments. [optional]  # noqa: E501
            s_ezsigntemplatesignature_attachmentdescription (str): The description attached to the attachment name added in Ezsigntemplatesignature of eEzsigntemplatesignatureType Attachments. [optional]  # noqa: E501
            e_ezsigntemplatesignature_attachmentnamesource (FieldEEzsigntemplatesignatureAttachmentnamesource): [optional]  # noqa: E501
            b_ezsigntemplatesignature_required (bool): Whether the Ezsigntemplatesignature is required or not. This field is relevant only with Ezsigntemplatesignature with eEzsigntemplatesignatureType = Attachments.. [optional]  # noqa: E501
            b_ezsigntemplatesignature_customdate (bool): Whether the Ezsigntemplatesignature has a custom date format or not. (Only possible when eEzsigntemplatesignatureType is **Name** or **Handwritten**). [optional]  # noqa: E501
            a_obj_ezsigntemplatesignaturecustomdate ([EzsigntemplatesignaturecustomdateResponseCompound]): An array of custom date blocks that will be filled at the time of signature.  Can only be used if bEzsigntemplatesignatureCustomdate is true.  Use an empty array if you don't want to have a date at all.. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
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
        """EzsigntemplatesignatureGetObjectV1ResponseMPayload - a model defined in OpenAPI

        Keyword Args:
            pki_ezsigntemplatesignature_id (FieldPkiEzsigntemplatesignatureID):
            fki_ezsigntemplatedocument_id (FieldPkiEzsigntemplatedocumentID):
            fki_ezsigntemplatesigner_id (FieldPkiEzsigntemplatesignerID):
            i_ezsigntemplatedocumentpage_pagenumber (FieldIEzsigntemplatedocumentpagePagenumber):
            i_ezsigntemplatesignature_x (FieldIEzsigntemplatesignatureX):
            i_ezsigntemplatesignature_y (FieldIEzsigntemplatesignatureY):
            i_ezsigntemplatesignature_step (FieldIEzsigntemplatesignatureStep):
            e_ezsigntemplatesignature_type (FieldEEzsigntemplatesignatureType):
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
            fki_ezsigntemplatesigner_id_validation (FieldPkiEzsigntemplatesignerID): [optional]  # noqa: E501
            t_ezsigntemplatesignature_tooltip (str): A tooltip that will be presented to Ezsigntemplatesigner about the Ezsigntemplatesignature. [optional]  # noqa: E501
            e_ezsigntemplatesignature_tooltipposition (FieldEEzsigntemplatesignatureTooltipposition): [optional]  # noqa: E501
            e_ezsigntemplatesignature_font (FieldEEzsigntemplatesignatureFont): [optional]  # noqa: E501
            i_ezsigntemplatesignature_validationstep (int): The step when the Ezsigntemplatesigner will be invited to validate the Ezsigntemplatesignature of eEzsigntemplatesignatureType Attachments. [optional]  # noqa: E501
            s_ezsigntemplatesignature_attachmentdescription (str): The description attached to the attachment name added in Ezsigntemplatesignature of eEzsigntemplatesignatureType Attachments. [optional]  # noqa: E501
            e_ezsigntemplatesignature_attachmentnamesource (FieldEEzsigntemplatesignatureAttachmentnamesource): [optional]  # noqa: E501
            b_ezsigntemplatesignature_required (bool): Whether the Ezsigntemplatesignature is required or not. This field is relevant only with Ezsigntemplatesignature with eEzsigntemplatesignatureType = Attachments.. [optional]  # noqa: E501
            b_ezsigntemplatesignature_customdate (bool): Whether the Ezsigntemplatesignature has a custom date format or not. (Only possible when eEzsigntemplatesignatureType is **Name** or **Handwritten**). [optional]  # noqa: E501
            a_obj_ezsigntemplatesignaturecustomdate ([EzsigntemplatesignaturecustomdateResponseCompound]): An array of custom date blocks that will be filled at the time of signature.  Can only be used if bEzsigntemplatesignatureCustomdate is true.  Use an empty array if you don't want to have a date at all.. [optional]  # noqa: E501
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
        # level we would get an error because the class level
        # code would be run when this module is imported, and these composed
        # classes don't exist yet because their module has not finished
        # loading
        lazy_import()
        return {
          'anyOf': [
          ],
          'allOf': [
              EzsigntemplatesignatureResponseCompound,
          ],
          'oneOf': [
          ],
        }
