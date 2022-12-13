from pyartnet import ArtNetNode
import asyncio

# Run this code in your async function
async def main():
    node = ArtNetNode('')
    #print(node)

    await node.start()

    # Create universe 0
    universe = node.add_universe(0)

    # Add a channel to the universe which consists of 3 values
    # Default size of a value is 8Bit (0..255) so this would fill
    # the DMX values 1..3 of the universe
    channel  = universe.add_channel(start=1, width=3)
    print(channel)

    # Fade channel to 255,0,0 in 5s
    # The fade will automatically run in the background
    channel.add_fade([255,0,0], 5000)

    # this can be used to wait till the fade is complete
    await channel.wait_till_fade_complete()

asyncio.run(main())