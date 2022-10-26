"""
    eZmax API Definition (Full)

    This API expose all the functionnalities for the eZmax and eZsign applications.  # noqa: E501

    The version of the OpenAPI document: 1.1.12
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
    from eZmaxApi.model.ezmaxinvoicingcommission_response_compound import EzmaxinvoicingcommissionResponseCompound
    from eZmaxApi.model.ezmaxinvoicingsummaryglobal_response import EzmaxinvoicingsummaryglobalResponse
    from eZmaxApi.model.ezmaxinvoicingsummaryglobal_response_compound_all_of import EzmaxinvoicingsummaryglobalResponseCompoundAllOf
    from eZmaxApi.model.field_d_ezmaxinvoicingsummaryglobal_countbilled import FieldDEzmaxinvoicingsummaryglobalCountbilled
    from eZmaxApi.model.field_d_ezmaxinvoicingsummaryglobal_countreal import FieldDEzmaxinvoicingsummaryglobalCountreal
    from eZmaxApi.model.field_d_ezmaxinvoicingsummaryglobal_net import FieldDEzmaxinvoicingsummaryglobalNet
    from eZmaxApi.model.field_d_ezmaxinvoicingsummaryglobal_partner import FieldDEzmaxinvoicingsummaryglobalPartner
    from eZmaxApi.model.field_d_ezmaxinvoicingsummaryglobal_rebateamount import FieldDEzmaxinvoicingsummaryglobalRebateamount
    from eZmaxApi.model.field_d_ezmaxinvoicingsummaryglobal_rebatepercent import FieldDEzmaxinvoicingsummaryglobalRebatepercent
    from eZmaxApi.model.field_d_ezmaxinvoicingsummaryglobal_rebatetotal import FieldDEzmaxinvoicingsummaryglobalRebatetotal
    from eZmaxApi.model.field_d_ezmaxinvoicingsummaryglobal_representative import FieldDEzmaxinvoicingsummaryglobalRepresentative
    from eZmaxApi.model.field_d_ezmaxinvoicingsummaryglobal_subtotal import FieldDEzmaxinvoicingsummaryglobalSubtotal
    from eZmaxApi.model.field_d_ezmaxinvoicingsummaryglobal_total import FieldDEzmaxinvoicingsummaryglobalTotal
    from eZmaxApi.model.field_i_ezmaxinvoicingsummaryglobal_days import FieldIEzmaxinvoicingsummaryglobalDays
    from eZmaxApi.model.field_pki_ezmaxinvoicing_id import FieldPkiEzmaxinvoicingID
    from eZmaxApi.model.field_pki_ezmaxinvoicingsummaryglobal_id import FieldPkiEzmaxinvoicingsummaryglobalID
    from eZmaxApi.model.field_pki_ezmaxproduct_id import FieldPkiEzmaxproductID
    globals()['EzmaxinvoicingcommissionResponseCompound'] = EzmaxinvoicingcommissionResponseCompound
    globals()['EzmaxinvoicingsummaryglobalResponse'] = EzmaxinvoicingsummaryglobalResponse
    globals()['EzmaxinvoicingsummaryglobalResponseCompoundAllOf'] = EzmaxinvoicingsummaryglobalResponseCompoundAllOf
    globals()['FieldDEzmaxinvoicingsummaryglobalCountbilled'] = FieldDEzmaxinvoicingsummaryglobalCountbilled
    globals()['FieldDEzmaxinvoicingsummaryglobalCountreal'] = FieldDEzmaxinvoicingsummaryglobalCountreal
    globals()['FieldDEzmaxinvoicingsummaryglobalNet'] = FieldDEzmaxinvoicingsummaryglobalNet
    globals()['FieldDEzmaxinvoicingsummaryglobalPartner'] = FieldDEzmaxinvoicingsummaryglobalPartner
    globals()['FieldDEzmaxinvoicingsummaryglobalRebateamount'] = FieldDEzmaxinvoicingsummaryglobalRebateamount
    globals()['FieldDEzmaxinvoicingsummaryglobalRebatepercent'] = FieldDEzmaxinvoicingsummaryglobalRebatepercent
    globals()['FieldDEzmaxinvoicingsummaryglobalRebatetotal'] = FieldDEzmaxinvoicingsummaryglobalRebatetotal
    globals()['FieldDEzmaxinvoicingsummaryglobalRepresentative'] = FieldDEzmaxinvoicingsummaryglobalRepresentative
    globals()['FieldDEzmaxinvoicingsummaryglobalSubtotal'] = FieldDEzmaxinvoicingsummaryglobalSubtotal
    globals()['FieldDEzmaxinvoicingsummaryglobalTotal'] = FieldDEzmaxinvoicingsummaryglobalTotal
    globals()['FieldIEzmaxinvoicingsummaryglobalDays'] = FieldIEzmaxinvoicingsummaryglobalDays
    globals()['FieldPkiEzmaxinvoicingID'] = FieldPkiEzmaxinvoicingID
    globals()['FieldPkiEzmaxinvoicingsummaryglobalID'] = FieldPkiEzmaxinvoicingsummaryglobalID
    globals()['FieldPkiEzmaxproductID'] = FieldPkiEzmaxproductID


class EzmaxinvoicingsummaryglobalResponseCompound(ModelComposed):
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
            'fki_ezmaxproduct_id': (FieldPkiEzmaxproductID,),  # noqa: E501
            's_ezmaxproduct_description_x': (str,),  # noqa: E501
            'dt_ezmaxinvoicingsummaryglobal_start': (str,),  # noqa: E501
            'dt_ezmaxinvoicingsummaryglobal_end': (str,),  # noqa: E501
            'i_ezmaxinvoicingsummaryglobal_days': (FieldIEzmaxinvoicingsummaryglobalDays,),  # noqa: E501
            'd_ezmaxinvoicingsummaryglobal_countreal': (FieldDEzmaxinvoicingsummaryglobalCountreal,),  # noqa: E501
            'd_ezmaxinvoicingsummaryglobal_countbilled': (FieldDEzmaxinvoicingsummaryglobalCountbilled,),  # noqa: E501
            'd_ezmaxinvoicingsummaryglobal_subtotal': (FieldDEzmaxinvoicingsummaryglobalSubtotal,),  # noqa: E501
            'd_ezmaxinvoicingsummaryglobal_rebateamount': (FieldDEzmaxinvoicingsummaryglobalRebateamount,),  # noqa: E501
            'd_ezmaxinvoicingsummaryglobal_rebatepercent': (FieldDEzmaxinvoicingsummaryglobalRebatepercent,),  # noqa: E501
            'd_ezmaxinvoicingsummaryglobal_rebatetotal': (FieldDEzmaxinvoicingsummaryglobalRebatetotal,),  # noqa: E501
            'd_ezmaxinvoicingsummaryglobal_total': (FieldDEzmaxinvoicingsummaryglobalTotal,),  # noqa: E501
            'b_ezmaxinvoicingsummaryglobal_adjustment': (bool,),  # noqa: E501
            'pki_ezmaxinvoicingsummaryglobal_id': (FieldPkiEzmaxinvoicingsummaryglobalID,),  # noqa: E501
            'fki_ezmaxinvoicing_id': (FieldPkiEzmaxinvoicingID,),  # noqa: E501
            'd_ezmaxinvoicingsummaryglobal_representative': (FieldDEzmaxinvoicingsummaryglobalRepresentative,),  # noqa: E501
            'd_ezmaxinvoicingsummaryglobal_partner': (FieldDEzmaxinvoicingsummaryglobalPartner,),  # noqa: E501
            'd_ezmaxinvoicingsummaryglobal_net': (FieldDEzmaxinvoicingsummaryglobalNet,),  # noqa: E501
            'a_obj_ezmaxinvoicingcommission': ([EzmaxinvoicingcommissionResponseCompound],),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'fki_ezmaxproduct_id': 'fkiEzmaxproductID',  # noqa: E501
        's_ezmaxproduct_description_x': 'sEzmaxproductDescriptionX',  # noqa: E501
        'dt_ezmaxinvoicingsummaryglobal_start': 'dtEzmaxinvoicingsummaryglobalStart',  # noqa: E501
        'dt_ezmaxinvoicingsummaryglobal_end': 'dtEzmaxinvoicingsummaryglobalEnd',  # noqa: E501
        'i_ezmaxinvoicingsummaryglobal_days': 'iEzmaxinvoicingsummaryglobalDays',  # noqa: E501
        'd_ezmaxinvoicingsummaryglobal_countreal': 'dEzmaxinvoicingsummaryglobalCountreal',  # noqa: E501
        'd_ezmaxinvoicingsummaryglobal_countbilled': 'dEzmaxinvoicingsummaryglobalCountbilled',  # noqa: E501
        'd_ezmaxinvoicingsummaryglobal_subtotal': 'dEzmaxinvoicingsummaryglobalSubtotal',  # noqa: E501
        'd_ezmaxinvoicingsummaryglobal_rebateamount': 'dEzmaxinvoicingsummaryglobalRebateamount',  # noqa: E501
        'd_ezmaxinvoicingsummaryglobal_rebatepercent': 'dEzmaxinvoicingsummaryglobalRebatepercent',  # noqa: E501
        'd_ezmaxinvoicingsummaryglobal_rebatetotal': 'dEzmaxinvoicingsummaryglobalRebatetotal',  # noqa: E501
        'd_ezmaxinvoicingsummaryglobal_total': 'dEzmaxinvoicingsummaryglobalTotal',  # noqa: E501
        'b_ezmaxinvoicingsummaryglobal_adjustment': 'bEzmaxinvoicingsummaryglobalAdjustment',  # noqa: E501
        'pki_ezmaxinvoicingsummaryglobal_id': 'pkiEzmaxinvoicingsummaryglobalID',  # noqa: E501
        'fki_ezmaxinvoicing_id': 'fkiEzmaxinvoicingID',  # noqa: E501
        'd_ezmaxinvoicingsummaryglobal_representative': 'dEzmaxinvoicingsummaryglobalRepresentative',  # noqa: E501
        'd_ezmaxinvoicingsummaryglobal_partner': 'dEzmaxinvoicingsummaryglobalPartner',  # noqa: E501
        'd_ezmaxinvoicingsummaryglobal_net': 'dEzmaxinvoicingsummaryglobalNet',  # noqa: E501
        'a_obj_ezmaxinvoicingcommission': 'a_objEzmaxinvoicingcommission',  # noqa: E501
    }

    read_only_vars = {
    }

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """EzmaxinvoicingsummaryglobalResponseCompound - a model defined in OpenAPI

        Keyword Args:
            fki_ezmaxproduct_id (FieldPkiEzmaxproductID):
            s_ezmaxproduct_description_x (str): The description of the Ezmaxproduct in the language of the requester
            dt_ezmaxinvoicingsummaryglobal_start (str): The start date for the Ezmaxinvoicingsummaryglobal
            dt_ezmaxinvoicingsummaryglobal_end (str): The end date for the Ezmaxinvoicingsummaryglobal
            i_ezmaxinvoicingsummaryglobal_days (FieldIEzmaxinvoicingsummaryglobalDays):
            d_ezmaxinvoicingsummaryglobal_countreal (FieldDEzmaxinvoicingsummaryglobalCountreal):
            d_ezmaxinvoicingsummaryglobal_countbilled (FieldDEzmaxinvoicingsummaryglobalCountbilled):
            d_ezmaxinvoicingsummaryglobal_subtotal (FieldDEzmaxinvoicingsummaryglobalSubtotal):
            d_ezmaxinvoicingsummaryglobal_rebateamount (FieldDEzmaxinvoicingsummaryglobalRebateamount):
            d_ezmaxinvoicingsummaryglobal_rebatepercent (FieldDEzmaxinvoicingsummaryglobalRebatepercent):
            d_ezmaxinvoicingsummaryglobal_rebatetotal (FieldDEzmaxinvoicingsummaryglobalRebatetotal):
            d_ezmaxinvoicingsummaryglobal_total (FieldDEzmaxinvoicingsummaryglobalTotal):
            b_ezmaxinvoicingsummaryglobal_adjustment (bool): Whether it is adjustment for the Ezmaxinvoicingsummaryglobal
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
            pki_ezmaxinvoicingsummaryglobal_id (FieldPkiEzmaxinvoicingsummaryglobalID): [optional]  # noqa: E501
            fki_ezmaxinvoicing_id (FieldPkiEzmaxinvoicingID): [optional]  # noqa: E501
            d_ezmaxinvoicingsummaryglobal_representative (FieldDEzmaxinvoicingsummaryglobalRepresentative): [optional]  # noqa: E501
            d_ezmaxinvoicingsummaryglobal_partner (FieldDEzmaxinvoicingsummaryglobalPartner): [optional]  # noqa: E501
            d_ezmaxinvoicingsummaryglobal_net (FieldDEzmaxinvoicingsummaryglobalNet): [optional]  # noqa: E501
            a_obj_ezmaxinvoicingcommission ([EzmaxinvoicingcommissionResponseCompound]): [optional]  # noqa: E501
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
        """EzmaxinvoicingsummaryglobalResponseCompound - a model defined in OpenAPI

        Keyword Args:
            fki_ezmaxproduct_id (FieldPkiEzmaxproductID):
            s_ezmaxproduct_description_x (str): The description of the Ezmaxproduct in the language of the requester
            dt_ezmaxinvoicingsummaryglobal_start (str): The start date for the Ezmaxinvoicingsummaryglobal
            dt_ezmaxinvoicingsummaryglobal_end (str): The end date for the Ezmaxinvoicingsummaryglobal
            i_ezmaxinvoicingsummaryglobal_days (FieldIEzmaxinvoicingsummaryglobalDays):
            d_ezmaxinvoicingsummaryglobal_countreal (FieldDEzmaxinvoicingsummaryglobalCountreal):
            d_ezmaxinvoicingsummaryglobal_countbilled (FieldDEzmaxinvoicingsummaryglobalCountbilled):
            d_ezmaxinvoicingsummaryglobal_subtotal (FieldDEzmaxinvoicingsummaryglobalSubtotal):
            d_ezmaxinvoicingsummaryglobal_rebateamount (FieldDEzmaxinvoicingsummaryglobalRebateamount):
            d_ezmaxinvoicingsummaryglobal_rebatepercent (FieldDEzmaxinvoicingsummaryglobalRebatepercent):
            d_ezmaxinvoicingsummaryglobal_rebatetotal (FieldDEzmaxinvoicingsummaryglobalRebatetotal):
            d_ezmaxinvoicingsummaryglobal_total (FieldDEzmaxinvoicingsummaryglobalTotal):
            b_ezmaxinvoicingsummaryglobal_adjustment (bool): Whether it is adjustment for the Ezmaxinvoicingsummaryglobal
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
            pki_ezmaxinvoicingsummaryglobal_id (FieldPkiEzmaxinvoicingsummaryglobalID): [optional]  # noqa: E501
            fki_ezmaxinvoicing_id (FieldPkiEzmaxinvoicingID): [optional]  # noqa: E501
            d_ezmaxinvoicingsummaryglobal_representative (FieldDEzmaxinvoicingsummaryglobalRepresentative): [optional]  # noqa: E501
            d_ezmaxinvoicingsummaryglobal_partner (FieldDEzmaxinvoicingsummaryglobalPartner): [optional]  # noqa: E501
            d_ezmaxinvoicingsummaryglobal_net (FieldDEzmaxinvoicingsummaryglobalNet): [optional]  # noqa: E501
            a_obj_ezmaxinvoicingcommission ([EzmaxinvoicingcommissionResponseCompound]): [optional]  # noqa: E501
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
              EzmaxinvoicingsummaryglobalResponse,
              EzmaxinvoicingsummaryglobalResponseCompoundAllOf,
          ],
          'oneOf': [
          ],
        }
