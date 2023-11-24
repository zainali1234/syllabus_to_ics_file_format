document.addEventListener('DOMContentLoaded', function () {
    var uploadInput = document.getElementById('upload');

    if (uploadInput) {
        uploadInput.addEventListener('change', function () {
            var fileInput = this;
            var fileName = fileInput.value.split('\\').pop(); // Get the file name

            if (/\.(pdf)$/i.test(fileName)) {
                var xhr = new XMLHttpRequest();
                xhr.open('POST', '/upload', true);

                // Create a FormData object and append the file to it
                var formData = new FormData();
                formData.append('file', fileInput.files[0]);

                // Set up the callback function to handle the server's response
                xhr.onload = function() {
                    if (xhr.status === 200) {
                        console.log('File successfully uploaded!');
                        var icsContent = xhr.responseText;
                        console.log(icsContent)
                        downloadICSFile(icsContent);
                    } else {
                        console.error('Error uploading file:', xhr.statusText);
                    }
                };

                // Send the FormData object with the file to the server
                xhr.send(formData);
            }
            else {
                alert("Please enter a pdf file.")
            }
        });
    } else {
        console.error('Element with ID "upload" not found.');
    }
});

function downloadICSFile(icsContent) {
      // Convert the iCal content to a Blob
    const blob = new Blob([icsContent], { type: 'text/calendar' });
  
    // Create a download link
    const link = document.createElement('a');
    link.href = URL.createObjectURL(blob);
    link.download = 'syllabi_conversion.ics';
  
    // Append the link to the document
    document.body.appendChild(link);
  
    // Trigger a click on the link to start the download
    link.click();
  
    // Remove the link from the document
    document.body.removeChild(link);
  }
  