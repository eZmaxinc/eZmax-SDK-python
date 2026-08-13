# EzsigntemplatepackagesignerRequestV2

A Ezsigntemplatepackagesigner Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezsigntemplatepackagesigner_id** | **int** | The unique ID of the Ezsigntemplatepackagesigner | [optional] 
**fki_ezsigntemplatepackage_id** | **int** | The unique ID of the Ezsigntemplatepackage | 
**fki_ezdoctemplatedocument_id** | **int** | The unique ID of the Ezdoctemplatedocument | [optional] 
**fki_user_id** | **int** | The unique ID of the User | [optional] 
**fki_usergroup_id** | **int** | The unique ID of the Usergroup | [optional] 
**e_ezsigntemplatepackagesigner_role** | [**FieldEEzsigntemplatepackagesignerRole**](FieldEEzsigntemplatepackagesignerRole.md) |  | [optional] 
**e_ezsigntemplatepackagesigner_mapping** | [**FieldEEzsigntemplatepackagesignerMapping**](FieldEEzsigntemplatepackagesignerMapping.md) |  | [optional] [default to FieldEEzsigntemplatepackagesignerMapping.MANUAL]
**s_ezsigntemplatepackagesigner_description** | **str** | The description of the Ezsigntemplatepackagesigner | 

## Example

```python
from eZmaxApi.models.ezsigntemplatepackagesigner_request_v2 import EzsigntemplatepackagesignerRequestV2

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplatepackagesignerRequestV2 from a JSON string
ezsigntemplatepackagesigner_request_v2_instance = EzsigntemplatepackagesignerRequestV2.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplatepackagesignerRequestV2.to_json())

# convert the object into a dict
ezsigntemplatepackagesigner_request_v2_dict = ezsigntemplatepackagesigner_request_v2_instance.to_dict()
# create an instance of EzsigntemplatepackagesignerRequestV2 from a dict
ezsigntemplatepackagesigner_request_v2_from_dict = EzsigntemplatepackagesignerRequestV2.from_dict(ezsigntemplatepackagesigner_request_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


