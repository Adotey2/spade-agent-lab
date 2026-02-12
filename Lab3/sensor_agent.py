import asyncio
from spade.agent import Agent
from spade.behaviour import CyclicBehaviour
from spade.message import Message
from environment import DisasterEnvironment
class SensorBehaviour(CyclicBehaviour):
    async def run(self):
        self.agent.environment.update_environment()
        percepts = self.agent.environment.sense()

        msg = Message(to="response@localhost")
        msg.body = str(percepts)
        await self.send(msg)

        print("[SensorAgent] Sent percepts:", percepts)

        await asyncio.sleep(5)



class SensorAgent(Agent):
    async def setup(self):
        print(f"[{self.jid}] SensorAgent started")
        self.environment = DisasterEnvironment()
        self.add_behaviour(SensorBehaviour())
