# AgentListElement

A Agent List Element

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_agent_id** | **int** | The unique ID of the Agent. | 
**fki_agenttype_id** | **int** | The unique ID of the Agenttype | 
**s_agenttype_name_x** | **str** | The name of the Agenttype in the language of the requester | 
**fki_agentincorporation_id** | **int** | The unique ID of the Agentincorporation. | [optional] 
**s_agentincorporation_name** | **str** | The name of the Agentincorporation | [optional] 
**fki_department_id** | **int** | The unique ID of the Department | 
**s_department_name_x** | **str** | The Name of the Department in the language of the requester | 
**fki_language_id** | **int** | The unique ID of the Language.  Valid values:  |Value|Description| |-|-| |1|French| |2|English| | 
**s_language_name_x** | **str** | The Name of the Language in the language of the requester | 
**s_realestateboardnumber_number** | **str** | The number of the Realestateboardnumber | [optional] 
**s_agent_code** | **str** | The code of the Agent | 
**i_agent_photocopiercode** | **int** | The photocopiercode of the Agent | 
**i_agent_longdistancecode** | **int** | The longdistancecode of the Agent | 
**i_agent_bannernumber** | **int** | The bannernumber of the Agent | 
**s_agent_realestateassociationlicense** | **str** | The realestateassociationlicense of the Agent | 
**dt_agent_hiredate** | **str** | The hiredate of the Agent | [optional] 
**dt_agent_leavedate** | **str** | The leavedate of the Agent | [optional] 
**b_agent_tranquillit** | **bool** | Whether if it&#39;s an tranquillit | 
**b_agent_residentiallicense** | **bool** | Whether if it&#39;s an residentiallicense | 
**b_agent_commerciallicense** | **bool** | Whether if it&#39;s an commerciallicense | 
**b_agent_mortgagelicense** | **bool** | Whether if it&#39;s an mortgagelicense | 
**b_agent_paidbyofficetranquillit** | **bool** | Whether if it&#39;s an paidbyofficetranquillit | 
**dt_agent_fintraccertification** | **str** | The fintraccertification of the Agent | [optional] 
**b_agent_isactive** | **bool** | Whether the Agent is active or not | 
**s_contact_firstname** | **str** | The First name of the contact | 
**s_contact_lastname** | **str** | The Last name of the contact | 
**dt_contact_birthdate** | **str** | The Birth Date of the contact | [optional] 
**s_email_address** | **str** | The email address. | [optional] 
**s_phone_e164** | **str** | A phone number in E.164 Format | [optional] 
**s_address_civic** | **str** | The Civic number. | [optional] 
**s_address_street** | **str** | The Street Name | [optional] 
**s_address_suite** | **str** | The Suite or appartment number | [optional] 
**s_address_city** | **str** | The City name | [optional] 
**s_address_zip** | **str** | The Postal/Zip Code  The value must be entered without spaces | [optional] 
**s_province_name_x** | **str** | The name of the Province in the language of the requester | [optional] 
**s_country_name_x** | **str** | The name of the Country in the language of the requester | [optional] 

## Example

```python
from eZmaxApi.models.agent_list_element import AgentListElement

# TODO update the JSON string below
json = "{}"
# create an instance of AgentListElement from a JSON string
agent_list_element_instance = AgentListElement.from_json(json)
# print the JSON string representation of the object
print(AgentListElement.to_json())

# convert the object into a dict
agent_list_element_dict = agent_list_element_instance.to_dict()
# create an instance of AgentListElement from a dict
agent_list_element_from_dict = AgentListElement.from_dict(agent_list_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


