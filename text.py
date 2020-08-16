# Please note use Nexmo for all of it.
import nexmo
client = nexmo.Client(api)

client.send_message({
    'from': 'from who',
    'to': 'the number to',
    'text': 'whatever text you want',
})
