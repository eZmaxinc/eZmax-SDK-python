# EzmaxpartnerproductstageListElement

A Ezmaxpartnerproductstage List Element

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezmaxpartnerproductstage_id** | **int** | The unique ID of the Ezmaxpartnerproductstage | 
**efks_ezmaxcustomer_code** | **str** | The Ezmaxcustomer code | 
**fki_ezmaxpartnerproduct_id** | **int** | The unique ID of the Ezmaxpartnerproduct | 
**s_ezmaxpartnerproduct_name_x** | **str** | The name of the Ezmaxpartnerproduct in the language of the requester | 
**s_ezmaxpartnerproduct_shortdescription_x** | **str** | The short description of the Ezmaxpartnerproduct in the language of the requester | 
**s_ezmaxpartnerproduct_logourl_x** | **str** | The url of the logo in the language of the requester | 
**fki_ezmaxpartner_id** | **int** | The unique ID of the Ezmaxpartner | 
**s_ezmaxpartner_name_x** | **str** | The name of the Ezmaxpartner in the language of the requester | 
**e_ezmaxpartnerproductstage_code** | [**FieldEEzmaxpartnerproductstageCode**](FieldEEzmaxpartnerproductstageCode.md) |  | 
**e_ezmaxpartnerproductstage_installationtype** | [**FieldEEzmaxpartnerproductstageInstallationtype**](FieldEEzmaxpartnerproductstageInstallationtype.md) |  | 
**b_ezmaxpartnerproductstage_published** | **bool** | Whether the Ezmaxpartnerproducstage is published or not | 
**b_ezmaxpartnerproductstage_installed** | **bool** | Whether the Ezmaxpartnerproductstage is installed or not | 

## Example

```python
from eZmaxApi.models.ezmaxpartnerproductstage_list_element import EzmaxpartnerproductstageListElement

# TODO update the JSON string below
json = "{}"
# create an instance of EzmaxpartnerproductstageListElement from a JSON string
ezmaxpartnerproductstage_list_element_instance = EzmaxpartnerproductstageListElement.from_json(json)
# print the JSON string representation of the object
print(EzmaxpartnerproductstageListElement.to_json())

# convert the object into a dict
ezmaxpartnerproductstage_list_element_dict = ezmaxpartnerproductstage_list_element_instance.to_dict()
# create an instance of EzmaxpartnerproductstageListElement from a dict
ezmaxpartnerproductstage_list_element_from_dict = EzmaxpartnerproductstageListElement.from_dict(ezmaxpartnerproductstage_list_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


