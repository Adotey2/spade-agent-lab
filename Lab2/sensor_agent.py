import asyncio
from spade.agent import Agent
from spade.behaviour import CyclicBehaviour
from environment import DisasterEnvironment
from event_logger import record_event


class EnvironmentMonitor(CyclicBehaviour):
    async def run(self):
        self.agent.env.update_environment()
        current_state = self.agent.env.sense()

        record_event(current_state)

        # Simple alert checks
        if current_state["temperature"] > 50:
            print("[SensorAgent] ⚠ Temperature is critically high")

        if current_state["smoke_level"] > 5:
            print("[SensorAgent] ⚠ Smoke levels are dangerous")

        if current_state["damage_severity"] >= 4:
            print("[SensorAgent] 🚨 Severe damage detected")

        await asyncio.sleep(5)


class SensorAgent(Agent):
    async def setup(self):
        print(f"[{self.jid}] Sensor agent running")
        self.env = DisasterEnvironment()
        self.add_behaviour(EnvironmentMonitor())


async def run_agent():
    sensor = SensorAgent("sensor@localhost", "password")
    await sensor.start()
    sensor.presence.set_available()

    await asyncio.sleep(30)

    await sensor.stop()


if __name__ == "__main__":
    asyncio.run(run_agent())
