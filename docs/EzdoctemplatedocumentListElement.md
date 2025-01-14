# EzdoctemplatedocumentListElement

A Ezdoctemplatedocument List Element

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezdoctemplatedocument_id** | **int** | The unique ID of the Ezdoctemplatedocument | 
**fki_language_id** | **int** | The unique ID of the Language.  Valid values:  |Value|Description| |-|-| |1|French| |2|English| | 
**fki_ezsignfoldertype_id** | **int** | The unique ID of the Ezsignfoldertype. | [optional] 
**fki_ezdoctemplatetype_id** | **int** | The unique ID of the Ezdoctemplatetype | 
**fki_ezdoctemplatefieldtypecategory_id** | **int** | The unique ID of the Ezdoctemplatefieldtypecategory | 
**s_ezsignfoldertype_name_x** | **str** | The name of the Ezsignfoldertype in the language of the requester | [optional] 
**s_ezdoctemplatetype_description_x** | **str** | The description of the Ezdoctemplatetype in the language of the requester | [optional] 
**s_ezdoctemplatefieldtypecategory_description_x** | **str** | The description of the Ezdoctemplatefieldtypecategory in the language of the requester | [optional] 
**e_ezdoctemplatedocument_privacylevel** | [**FieldEEzdoctemplatedocumentPrivacylevel**](FieldEEzdoctemplatedocumentPrivacylevel.md) |  | [optional] 
**b_ezdoctemplatedocument_isactive** | **bool** | Whether the ezdoctemplatedocument is active or not | 
**s_ezdoctemplatedocument_name_x** | **str** | The name of the Ezdoctemplatedocument in the language of the requester | 

## Example

```python
from eZmaxApi.models.ezdoctemplatedocument_list_element import EzdoctemplatedocumentListElement

# TODO update the JSON string below
json = "{}"
# create an instance of EzdoctemplatedocumentListElement from a JSON string
ezdoctemplatedocument_list_element_instance = EzdoctemplatedocumentListElement.from_json(json)
# print the JSON string representation of the object
print(EzdoctemplatedocumentListElement.to_json())

# convert the object into a dict
ezdoctemplatedocument_list_element_dict = ezdoctemplatedocument_list_element_instance.to_dict()
# create an instance of EzdoctemplatedocumentListElement from a dict
ezdoctemplatedocument_list_element_from_dict = EzdoctemplatedocumentListElement.from_dict(ezdoctemplatedocument_list_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


