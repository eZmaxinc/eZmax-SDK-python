# EzsigntemplateRequestCompoundV2

A Ezsigntemplate Object and children

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezsigntemplate_id** | **int** | The unique ID of the Ezsigntemplate | [optional] 
**fki_ezsignfoldertype_id** | **int** | The unique ID of the Ezsignfoldertype. | [optional] 
**fki_language_id** | **int** | The unique ID of the Language.  Valid values:  |Value|Description| |-|-| |1|French| |2|English| | 
**s_ezsigntemplate_description** | **str** | The description of the Ezsigntemplate | 
**s_ezsigntemplate_filenamepattern** | **str** | The filename pattern of the Ezsigntemplate | [optional] 
**b_ezsigntemplate_adminonly** | **bool** | Whether the Ezsigntemplate can be accessed by admin users only (eUserType&#x3D;Normal) | 
**e_ezsigntemplate_type** | [**FieldEEzsigntemplateType**](FieldEEzsigntemplateType.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigntemplate_request_compound_v2 import EzsigntemplateRequestCompoundV2

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplateRequestCompoundV2 from a JSON string
ezsigntemplate_request_compound_v2_instance = EzsigntemplateRequestCompoundV2.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplateRequestCompoundV2.to_json())

# convert the object into a dict
ezsigntemplate_request_compound_v2_dict = ezsigntemplate_request_compound_v2_instance.to_dict()
# create an instance of EzsigntemplateRequestCompoundV2 from a dict
ezsigntemplate_request_compound_v2_form_dict = ezsigntemplate_request_compound_v2.from_dict(ezsigntemplate_request_compound_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


