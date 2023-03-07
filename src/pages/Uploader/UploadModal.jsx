import React from 'react';

const UploadModal = ({notes=[],handleChange,setShowUploaderModal,handleSubmit}) => {
    return (
        <div className="fixed z-10 inset-0 overflow-y-auto modal-main">
          <div className="flex items-center justify-center min-h-screen">
            <div className="relative bg-white rounded-lg overflow-hidden shadow-xl text-center mx-4 md:mx-0 md:w-[640px]">
              <button className='absolute right-[39px] top-[39px] font-bold' onClick={()=>setShowUploaderModal(false)}>X</button>
              <h4 className="modal-title not-italic text-xl font-bold mb-2 mt-14 text-center">Complete Your Upload</h4>
              <h3 className='modal-sub-title mt-2 not-italic font-normal text-base'>Fill in the details below to complete your upload</h3>
              <form className='mt-6 mx-[72px]' onSubmit={handleSubmit}>
                <div className='select-wrapper'>
                  <select className="field-color w-full px-6 py-2 rounded-lg" onChange={handleChange} defaultValue={"default"} id="noteType"  name="noteType"  aria-expanded="true">
                    <option value="default" disabled>Select note type</option>
                    {notes.map((type) => (
                      <option value={type.value} key={type.value}>
                        {type.label}
                      </option>
                    ))}
                  </select>
                </div>
                <div className="mb-4">
                  <input
                    onChange={handleChange}
                    type="text"
                    id="name"
                    name="name"
                    className="field-color mt-[72px] py-2 px-6 w-full"
                    placeholder="Enter client name"
                  />
                </div>
                <div className="">
                  <button type="submit" className="modal-button p-4 text-white mb-4 mx-auto mt-20 font-bold rounded-lg">
                    Finish Upload
                  </button>
                </div>
              </form>
            </div>
          </div>
        </div>
    );
};

export default UploadModal;