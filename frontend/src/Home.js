import React, { Component } from 'react'
import axios from 'axios'

class Home extends Component {
    state={
        datas:[]
    }
    componentDidMount(){
        axios.get('http://127.0.0.1:8000/api/')
        .then(res =>{
            this.setState(
                {
                    datas:res.data
                }
            )
            console.log(res.data);
        })
    }
    render() {
        return (
        <div>
             Posts
        </div>
        )
    }
}

export default Home