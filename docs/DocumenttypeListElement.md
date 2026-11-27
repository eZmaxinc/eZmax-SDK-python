# DocumenttypeListElement

A Documenttype List Element

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_documenttype_id** | **int** | The unique ID of the Documenttype | 
**s_documenttype_name_x** | **str** | The name of the document type in the requester&#39;s language | 
**s_documenttype_defaultfilename** | **str** | The default filename for the document type | 
**b_documenttype_showagent** | **bool** | Whether the document type should be shown to the agent | 
**b_documenttype_isactive** | **bool** | Whether the documenttype is active or not | 
**b_documenttype_sale** | **bool** | Whether the document type applies to sale transactions | 
**b_documenttype_rental** | **bool** | Whether the document type applies to rental transactions | 
**b_documenttype_reference** | **bool** | Whether the document type is a reference document | 
**b_documenttype_mortgagereference** | **bool** | Whether the document type is a mortgage reference | 
**b_documenttype_evaluation** | **bool** | Whether the document type applies to evaluation transactions | 
**b_documenttype_consultation** | **bool** | Whether the document type applies to consultation transactions | 
**b_documenttype_otherservices** | **bool** | Whether the document type applies to other services | 
**b_documenttype_foreclosedsale** | **bool** | Whether the document type applies to foreclosed sale transactions | 
**b_documenttype_commercialfunding** | **bool** | Whether the document type applies to commercial funding transactions | 
**b_documenttype_canafe** | **bool** | Whether the document type applies to Canafe transactions | 
**e_documenttype_ezcom** | [**FieldEDocumenttypeEzcom**](FieldEDocumenttypeEzcom.md) |  | [optional] 
**e_documenttype_privacydefault** | [**FieldEDocumenttypePrivacydefault**](FieldEDocumenttypePrivacydefault.md) |  | 
**e_documenttype_statusdefault** | [**FieldEDocumenttypeStatusdefault**](FieldEDocumenttypeStatusdefault.md) |  | 
**e_documenttype_salebyowner** | [**FieldEDocumenttypeSalebyowner**](FieldEDocumenttypeSalebyowner.md) |  | 
**e_documenttype_saledisplaybyrole** | [**FieldEDocumenttypeSaledisplaybyrole**](FieldEDocumenttypeSaledisplaybyrole.md) |  | 
**e_documenttype_transactiontype** | [**FieldEDocumenttypeTransactiontype**](FieldEDocumenttypeTransactiontype.md) |  | 
**e_documenttype_repossession** | [**FieldEDocumenttypeRepossession**](FieldEDocumenttypeRepossession.md) |  | 

## Example

```python
from eZmaxApi.models.documenttype_list_element import DocumenttypeListElement

# TODO update the JSON string below
json = "{}"
# create an instance of DocumenttypeListElement from a JSON string
documenttype_list_element_instance = DocumenttypeListElement.from_json(json)
# print the JSON string representation of the object
print(DocumenttypeListElement.to_json())

# convert the object into a dict
documenttype_list_element_dict = documenttype_list_element_instance.to_dict()
# create an instance of DocumenttypeListElement from a dict
documenttype_list_element_from_dict = DocumenttypeListElement.from_dict(documenttype_list_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


