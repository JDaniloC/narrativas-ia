import React from 'react';
import VideoSlide from "./components/videos";

export default async function IndexPage() {

  return (
    <div className='flex items-center justify-center flex-col'>
      <h1 className='white font-bold text-6xl m-4 mb-10'>
        Narrativas AI
      </h1>
      <div className="max-w-4xl">
        <VideoSlide />
      </div>
    </div>
  )
}
