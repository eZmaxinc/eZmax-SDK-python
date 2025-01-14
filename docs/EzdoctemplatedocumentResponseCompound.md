# EzdoctemplatedocumentResponseCompound

A Ezdoctemplatedocument Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezdoctemplatedocument_id** | **int** | The unique ID of the Ezdoctemplatedocument | 
**fki_language_id** | **int** | The unique ID of the Language.  Valid values:  |Value|Description| |-|-| |1|French| |2|English| | 
**fki_ezsignfoldertype_id** | **int** | The unique ID of the Ezsignfoldertype. | [optional] 
**fki_ezdoctemplatetype_id** | **int** | The unique ID of the Ezdoctemplatetype | 
**fki_ezdoctemplatefieldtypecategory_id** | **int** | The unique ID of the Ezdoctemplatefieldtypecategory | 
**e_ezdoctemplatedocument_privacylevel** | [**FieldEEzdoctemplatedocumentPrivacylevel**](FieldEEzdoctemplatedocumentPrivacylevel.md) |  | [optional] 
**b_ezdoctemplatedocument_isactive** | **bool** | Whether the ezdoctemplatedocument is active or not | 
**obj_ezdoctemplatedocument_name** | [**MultilingualEzdoctemplatedocumentName**](MultilingualEzdoctemplatedocumentName.md) |  | 
**s_ezdoctemplatedocument_name_x** | **str** | The name of the Ezdoctemplatedocument in the language of the requester | [optional] 
**s_ezsignfoldertype_name_x** | **str** | The name of the Ezsignfoldertype in the language of the requester | [optional] 
**s_ezdoctemplatefieldtypecategory_description_x** | **str** | The description of the Ezdoctemplatefieldtypecategory in the language of the requester | 
**s_ezdoctemplatetype_description_x** | **str** | The description of the Ezdoctemplatetype in the language of the requester | 

## Example

```python
from eZmaxApi.models.ezdoctemplatedocument_response_compound import EzdoctemplatedocumentResponseCompound

# TODO update the JSON string below
json = "{}"
# create an instance of EzdoctemplatedocumentResponseCompound from a JSON string
ezdoctemplatedocument_response_compound_instance = EzdoctemplatedocumentResponseCompound.from_json(json)
# print the JSON string representation of the object
print(EzdoctemplatedocumentResponseCompound.to_json())

# convert the object into a dict
ezdoctemplatedocument_response_compound_dict = ezdoctemplatedocument_response_compound_instance.to_dict()
# create an instance of EzdoctemplatedocumentResponseCompound from a dict
ezdoctemplatedocument_response_compound_from_dict = EzdoctemplatedocumentResponseCompound.from_dict(ezdoctemplatedocument_response_compound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


