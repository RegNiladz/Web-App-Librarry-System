    //const { error } = require('console');
    //const { stdout, stderr } = require('process');
    const { spawn } = require('child_process');
    class generate_qr{

        constructor(qrfile_name, qrfile_path){
            this.qrfile_name = qrfile_name;
            this.qrfile_path = qrfile_path;
        }
        make_qr(){
            //const { spawn } = require('child_process');
            const qr_script = `python`;
            const execute_pythoncode = spawn('python3', ["qrgen.py", this.qrfile_name, this.qrfile_path]);

            execute_pythoncode.stdout.on('data', (data) => {
                console.log(`stdout: ${data}`);
            });
    
            execute_pythoncode.stderr.on('data', (data) => {
                console.error(`stderr: ${data}`);
            });
    
            execute_pythoncode.on('close', (code) => {
                console.log(`child process exited with code ${code}`);
            });
        }
    }
    qr_object = new generate_qr("javascripttest", "qr_pictures");
    qr_object.make_qr();


