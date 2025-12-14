import subprocess
import base64

class ExecutionModule:

    def run_cmd(self, cmd):
        try:
            return subprocess.check_output(cmd, shell=True, text=True)
        except subprocess.CalledProcessError as e:
            return e.output

    def run_powershell(self, ps_cmd):
        command = f"powershell -Command \"{ps_cmd}\""
        return self.run_cmd(command)

    def run_encoded_powershell(self, ps_cmd):
        encoded = base64.b64encode(ps_cmd.encode('utf-16le')).decode()
        command = f"powershell -EncodedCommand {encoded}"
        return self.run_cmd(command)
