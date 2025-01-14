# EzdoctemplatedocumentRequestPatch

An Ezdoctemplatedocument Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**e_ezdoctemplatedocument_format** | **str** | Indicates the format of the template.  This field is Required when sEzdoctemplatedocumentBase64 is set. | [optional] 
**s_ezdoctemplatedocument_fields** | **str** | List of field in Ezdoctemplatedocument | [optional] 
**s_ezdoctemplatedocument_base64** | **bytearray** | The Base64 encoded binary content of the document.  This field is Required when eEzdoctemplatedocumentFormat is set. | [optional] 

## Example

```python
from eZmaxApi.models.ezdoctemplatedocument_request_patch import EzdoctemplatedocumentRequestPatch

# TODO update the JSON string below
json = "{}"
# create an instance of EzdoctemplatedocumentRequestPatch from a JSON string
ezdoctemplatedocument_request_patch_instance = EzdoctemplatedocumentRequestPatch.from_json(json)
# print the JSON string representation of the object
print(EzdoctemplatedocumentRequestPatch.to_json())

# convert the object into a dict
ezdoctemplatedocument_request_patch_dict = ezdoctemplatedocument_request_patch_instance.to_dict()
# create an instance of EzdoctemplatedocumentRequestPatch from a dict
ezdoctemplatedocument_request_patch_from_dict = EzdoctemplatedocumentRequestPatch.from_dict(ezdoctemplatedocument_request_patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


