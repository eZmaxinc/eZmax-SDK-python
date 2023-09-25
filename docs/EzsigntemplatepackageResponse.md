# EzsigntemplatepackageResponse

A Ezsigntemplatepackage Object

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezsigntemplatepackage_id** | **int** | The unique ID of the Ezsigntemplatepackage | 
**fki_ezsignfoldertype_id** | **int** | The unique ID of the Ezsignfoldertype. | 
**fki_language_id** | **int** | The unique ID of the Language.  Valid values:  |Value|Description| |-|-| |1|French| |2|English| | 
**s_language_name_x** | **str** | The Name of the Language in the language of the requester | 
**s_ezsigntemplatepackage_description** | **str** | The description of the Ezsigntemplatepackage | 
**b_ezsigntemplatepackage_adminonly** | **bool** | Whether the Ezsigntemplatepackage can be accessed by admin users only (eUserType&#x3D;Normal) | 
**b_ezsigntemplatepackage_needvalidation** | **bool** | Whether the Ezsignbulksend was automatically modified and needs a manual validation | 
**b_ezsigntemplatepackage_isactive** | **bool** | Whether the Ezsigntemplatepackage is active or not | 
**s_ezsignfoldertype_name_x** | **str** | The name of the Ezsignfoldertype in the language of the requester | 

## Example

```python
from eZmaxApi.models.ezsigntemplatepackage_response import EzsigntemplatepackageResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplatepackageResponse from a JSON string
ezsigntemplatepackage_response_instance = EzsigntemplatepackageResponse.from_json(json)
# print the JSON string representation of the object
print EzsigntemplatepackageResponse.to_json()

# convert the object into a dict
ezsigntemplatepackage_response_dict = ezsigntemplatepackage_response_instance.to_dict()
# create an instance of EzsigntemplatepackageResponse from a dict
ezsigntemplatepackage_response_form_dict = ezsigntemplatepackage_response.from_dict(ezsigntemplatepackage_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


