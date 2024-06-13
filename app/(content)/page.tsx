import React from 'react';
import VideoSlide from "./components/videos";

export default async function IndexPage() {

  return (
    <div className='flex items-center justify-center'>
      <div className="max-w-4xl">
        <VideoSlide />
      </div>
    </div>
  )
}
