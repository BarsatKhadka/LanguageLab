import React from 'react'
import {motion , useAnimation} from 'framer-motion'

export default function Box6() {
 const control = useAnimation()
  return (
      <div className='box-container'>
        <button onClick= { () => control.start({
            x:1500,
            transition: {duration : 2}
        })}
        
        >Move Right</button>
        <button onClick={() =>{
            control.start({
                y: -1500,
                transition: {duration: 2}
            })
        }}>Move Top</button>
        <button onClick = {() =>{
            control.start({
                    borderRadius: "50%",
                    transition: {duration: 2}
                
            })
        }}>Circle</button>
        <button>Square</button>
        <button onClick={() => control.stop()}>Stop</button>


        <motion.div className='box'
        animate={control}
        >Click Me

        </motion.div>
    </div>
  )
}
