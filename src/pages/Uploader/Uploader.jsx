import React, { useState } from 'react';

const notes = [
  { value: "typeA", label: "type A" },
  { value: "typeB", label: "type B" },
  { value: "typeC", label: "type C" },
];


const Uploader = () => {
  const [showUploaderModal, setShowUploaderModal] = useState(false);
  const [uploadedFiles, setUploadedFiles] = useState([]);
  const [progressBars, setProgressBars] = useState([]);
  
    return (
        <>
            <div className="container mx-auto px-4 py-8">
              {/* <div className="flex items-center justify-center"> */}
              <div className="">
                <div>
                  <div className="flex items-center justify-between mt-8">
                    <h1>Hi, Maria</h1>
                    <img width="18px" src={"/images/Help.png"} alt="" />
                  </div>
                  <h1 className="text-2xl font-bold text-start mb-4 container mt-6">
                    Upload your session’s recordings
                  </h1>

                  <div className="flex justify-center mb-4 mt-6 not-italic font-bold text-base leading-6 text-white">
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

      {!showUploaderModal && (
        <div className="fixed z-10 inset-0 overflow-y-auto modal-main">
          <div className="flex items-center justify-center min-h-screen">
            <div className="bg-white rounded-lg overflow-hidden shadow-xl text-center w-[640px]">
              <h4 className="modal-title not-italic text-xl font-bold mb-2 mt-14 text-center">Complete Your Upload</h4>
              <h3 className='modal-sub-title mt-2 not-italic font-normal text-base'>Fill in the details below to complete your upload</h3>
              <form className='mt-6 mx-[72px]'>
                  <select className="modal-select w-full px-6 py-2 rounded-lg" id="noteType"  name="noteType"  >
                    <option value="">Progress note</option>
                    {notes.map((type) => (
                      <option value={type.value} key={type.value}>
                        {type.label}
                      </option>
                    ))}
                  </select>
                <div className="mb-4">
                  {/* <label htmlFor="name" className="block font-bold mb-2">
                    Name
                  </label> */}
                  <input
                    type="text"
                    id="name"
                    name="name"
                    className=" modal-select"
                    placeholder="Enter client name"
                  />
                </div>
                <div className="flex items-center justify-center">
                  <button type="submit" className="modal-button">
                    Finish Upload
                  </button>
                </div>
              </form>
            </div>
          </div>
        </div>
      )}

      {uploadedFiles.length > 0 && (
        <div className="mt-8 flex items-center justify-center">
          <div>
            <div className="not-progess">
              <h2>
                {" "}
                <span>2</span> Notes in progress
              </h2>
            </div>

            {/* <h2 className="text-xl font-bold mb-4">Uploaded Files</h2> */}

            <ul>
              <div className="">
                <table className="table-main">
                  <thead>
                    <tr>
                      <th>Client</th>
                      <th className="delete-btn">Type</th>
                      <th>ETA</th>
                    </tr>
                  </thead>

                  <tbody>
                  {uploadedFiles.map((file) => (
                    <tr className="tabel-row">
                      <td>{file.name}</td>
                      <td className="delete-btn">{file.noteType}</td>
                      <td>
                        {" "}
                        <div className="flex-1">
                          <div className="h-6 bg-gray-300 rounded-full">
                            <div
                              className={`h-6 bg-green-500 rounded-full ${
                                progressBars.find((bar) => bar.id === file.id)
                                  ?.progress === null && "w-full"
                              }`}
                              style={{
                                width: `${
                                  progressBars?.find(
                                    (bar) => bar.id === file.id
                                  )?.progress
                                }%`,
                              }}
                            ></div>
                          </div>
                        </div>
                      </td>
                      <td>
                        {" "}
                        <button
                          className="ml-4 hover:text-red-700 delete-btn"
                        >
                          <img src={"/images/delete.png"} width="24px" alt="" />
                        </button>
                      </td>
                    </tr>
                       ))}
                  </tbody>
                </table>
              </div>
              
            </ul>
          </div>
        </div>
      )}
    </div>
        </>
        
    );
};

export default Uploader;