# EzsigntemplatepackagesignerResponse

A Ezsigntemplatepackagesigner Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezsigntemplatepackagesigner_id** | **int** | The unique ID of the Ezsigntemplatepackagesigner | 
**fki_ezsigntemplatepackage_id** | **int** | The unique ID of the Ezsigntemplatepackage | 
**fki_ezdoctemplatedocument_id** | **int** | The unique ID of the Ezdoctemplatedocument | [optional] 
**fki_user_id** | **int** | The unique ID of the User | [optional] 
**fki_usergroup_id** | **int** | The unique ID of the Usergroup | [optional] 
**s_ezdoctemplatedocument_name_x** | **str** | The name of the Ezdoctemplatedocument in the language of the requester | [optional] 
**b_ezsigntemplatepackagesigner_receivecopy** | **bool** | If this flag is true. The signatory will receive a copy of every signed Ezsigndocument even if it ain&#39;t required to sign the document. | [optional] 
**e_ezsigntemplatepackagesigner_mapping** | [**FieldEEzsigntemplatepackagesignerMapping**](FieldEEzsigntemplatepackagesignerMapping.md) |  | [optional] [default to FieldEEzsigntemplatepackagesignerMapping.MANUAL]
**s_ezsigntemplatepackagesigner_description** | **str** | The description of the Ezsigntemplatepackagesigner | 
**s_user_name** | **str** | The description of the User in the language of the requester | [optional] 
**s_usergroup_name_x** | **str** | The Name of the Usergroup in the language of the requester | [optional] 

## Example

```python
from eZmaxApi.models.ezsigntemplatepackagesigner_response import EzsigntemplatepackagesignerResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplatepackagesignerResponse from a JSON string
ezsigntemplatepackagesigner_response_instance = EzsigntemplatepackagesignerResponse.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplatepackagesignerResponse.to_json())

# convert the object into a dict
ezsigntemplatepackagesigner_response_dict = ezsigntemplatepackagesigner_response_instance.to_dict()
# create an instance of EzsigntemplatepackagesignerResponse from a dict
ezsigntemplatepackagesigner_response_from_dict = EzsigntemplatepackagesignerResponse.from_dict(ezsigntemplatepackagesigner_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


