# EzdoctemplatedocumentRequest

A Ezdoctemplatedocument Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezdoctemplatedocument_id** | **int** | The unique ID of the Ezdoctemplatedocument | [optional] 
**fki_language_id** | **int** | The unique ID of the Language.  Valid values:  |Value|Description| |-|-| |1|French| |2|English| | 
**fki_ezsignfoldertype_id** | **int** | The unique ID of the Ezsignfoldertype. | [optional] 
**fki_ezdoctemplatetype_id** | **int** | The unique ID of the Ezdoctemplatetype | 
**fki_ezdoctemplatefieldtypecategory_id** | **int** | The unique ID of the Ezdoctemplatefieldtypecategory | 
**e_ezdoctemplatedocument_privacylevel** | [**FieldEEzdoctemplatedocumentPrivacylevel**](FieldEEzdoctemplatedocumentPrivacylevel.md) |  | [optional] 
**b_ezdoctemplatedocument_isactive** | **bool** | Whether the ezdoctemplatedocument is active or not | 
**obj_ezdoctemplatedocument_name** | [**MultilingualEzdoctemplatedocumentName**](MultilingualEzdoctemplatedocumentName.md) |  | 

## Example

```python
from eZmaxApi.models.ezdoctemplatedocument_request import EzdoctemplatedocumentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EzdoctemplatedocumentRequest from a JSON string
ezdoctemplatedocument_request_instance = EzdoctemplatedocumentRequest.from_json(json)
# print the JSON string representation of the object
print(EzdoctemplatedocumentRequest.to_json())

# convert the object into a dict
ezdoctemplatedocument_request_dict = ezdoctemplatedocument_request_instance.to_dict()
# create an instance of EzdoctemplatedocumentRequest from a dict
ezdoctemplatedocument_request_from_dict = EzdoctemplatedocumentRequest.from_dict(ezdoctemplatedocument_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


