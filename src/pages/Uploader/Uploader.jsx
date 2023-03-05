import React from 'react';

const Uploader = () => {
    
    return (
        <div>
            <h1>File Upload</h1>
            <div>
                <button>
                Upload
                </button>
            </div>
            <div >
          <div >
            <div >
              <h2 > File Uploader</h2>
              <form>
                <div >
                  <label htmlFor="" id=''> Type </label>
                  <select  id="" name="type">
                      <option value="">Select  Type</option>
                  </select>
                </div>
                <div >
                  <label>name </label>
                  <input type="text" id="name" name="name" />
                </div>
                <button type="submit" >button</button>
              </form>
            </div>
          </div>
        </div>
        </div>
        
    );
};

export default Uploader;