import React, { useEffect, useState } from 'react';
import UploadModal from './UploadModal';

const notes = [
  { value: "Progress note", label: "Progress note - 80 left" },
  { value: "Soap note", label: "Soap note - 80 left" },
  { value: "EMDR note", label: "EMDR note - 80 left" },
  { value: "Couples therapy", label: "Couples therapy note - 80 left" },
  { value: "Family therapy", label: "Family therapy note - 80 left" },
];


const Uploader = () => {
  const [showUploaderModal, setShowUploaderModal] = useState(false);
  const [formTemvalues, setFormTemvalues] = useState({noteType: "",name: "",});
  const [uploadedFiles, setUploadedFiles] = useState([]);
  const [progressBars, setProgressBars] = useState([]);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormTemvalues({ ...formTemvalues, [name]: value });
  };
  // uoload file handler 
  const handleSubmit = (e) => {
    e.preventDefault();
    const newId = uploadedFiles.length + 1;
    const newFile = {
      id: newId,
      name: formTemvalues.name,
      noteType: formTemvalues.noteType,
      progress: 0, // initialize progress to 0
    };
    setUploadedFiles([...uploadedFiles, newFile]);
    setFormTemvalues({ noteType: "", name: "" });
    setShowUploaderModal(false);
    setProgressBars([...progressBars,{ id: newId, progress: 0 }]);
  };

  //  delete file handler
  const handleDelete = (id) => {
    const remainingProgress = progressBars.filter((bar) => bar.id !== id);
    setProgressBars(remainingProgress);
    const remainingUploadFiles = uploadedFiles.filter((file) => file.id !== id);
    setUploadedFiles(remainingUploadFiles);
  };

  
  useEffect(() => {
    const intervalId = setInterval(() => {
      if (progressBars.length) {
        setProgressBars((bars) =>
          bars.map((bar) => ({
            ...bar,
            progress: bar.progress === 100 ? null : bar.progress + 10,
          }))
        );
      } else {
        clearInterval(intervalId);
      }
      
      // Check if any files have reached 100% completion
      const completedFiles = uploadedFiles.filter((file) =>progressBars.some((bar) => bar.id === file.id && bar.progress === 100));
      if (completedFiles.length) {
        // Remove the completed files from the `files` state
        setUploadedFiles((prev) =>prev.filter((file) => !completedFiles.some((completed) => completed.id === file.id)));
        // Remove the completed progress bars from the `progressBars` state
        setProgressBars((bars) =>bars.filter((bar) => !completedFiles.some((completed) => completed.id === bar.id)));
      }
  
      // Check if all progress bars have reached 100%
      const allComplete = progressBars.every((bar) => bar.progress === 100);
      if (allComplete) {
        clearInterval(intervalId);
      }
    }, 2000);
  
    return () => clearInterval(intervalId);
  }, [progressBars, uploadedFiles]);
  
  
    return (
        <>
            <div className="container mx-auto px-4 py-8">
              <div className="">
                <div>
                  <div className="flex items-center justify-between mt-4 md:mt-8">
                    <h1 className='montserrat font-medium text-xl leading-6'>Hi, Maria</h1>
                    <img width="18px" src={"/images/Help.png"} alt="" />
                  </div>
                  <h1 className="text-2xl font-bold text-start mb-4 container mt-4 md:mt-6">
                    Upload your session’s recordings
                  </h1>

                  <div className="flex justify-center mb-4 mt-16 md:mt-6 not-italic font-bold text-base leading-6 text-white">
                    <button
                      // className="upload-button"
                      className="upload-button w-full h-10 rounded-lg "
                      onClick={() => setShowUploaderModal(true)}
                    >
                      Upload
                    </button>
                  </div>
                </div>
              </div>

              {showUploaderModal && <UploadModal notes={notes} handleSubmit={handleSubmit} handleChange={handleChange} setShowUploaderModal={setShowUploaderModal} />}

            {uploadedFiles.length > 0 && (
              <div className="mt-[200px] md:mt-[116px]">
                <div>
                  <div className="note-progess h-10 md:h-12 flex items-center">
                    <div className='flex items-center'>
                      <div className='rounded-full ml-[35px] w-8 h-8 flex justify-center items-center'>{progressBars.length}</div>
                    </div>
                    <h2 className='ml-6 md:ml-2 text-[20px] text-black font-medium'>Notes in progress</h2>
                  </div>
                  <div className=" mt-4">
                    <table className="table-main w-full text-left text-black">
                      <thead>
                        <tr>
                          <th>Client</th>
                          <th className="hidden md:block">Type</th>
                          <th>ETA</th>
                        </tr>
                      </thead>
                      <tbody className='mt-8'>
                      {uploadedFiles.map((file) => (
                        <tr className="tabel-row rounded-lg  my-[5px]">
                          <td className='pl-10 py-3 text-base font-normal w-52 md:w-fit'>{file.name}</td>
                          <td className="hidden md:block py-3">{file.noteType}</td>
                          <td className='pr-2 md:pr-0'>
                            <div className="flex-1">
                              <div className="h-6 bg-gray-300 rounded-full overflow-hidden">
                                <div
                                  className={`h-6 bg-green-500 rounded-full`}
                                  style={{width: `${progressBars?.find((bar) => bar.id === file.id)?.progress}%`,}}
                                ></div>
                              </div>
                            </div>
                          </td>
                          <td className='rounded-r-lg w-40 hidden md:table-cell'>
                            <div className='flex justify-end mr-12'>
                              <button className=" hover:text-red-700" onClick={()=>handleDelete(file.id)}>
                                <img src={"/images/delete.png"} width="24px" alt="" />
                              </button>
                            </div>
                          </td>
                        </tr>
                          ))}
                      </tbody>
                    </table>
                  </div>
                </div>
              </div>
            )}
          </div>
        </>
        
    );
};

export default Uploader;