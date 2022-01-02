import React , { useState, useEffect }from "react";
import {Container,Row,ListGroup} from "react-bootstrap";
import UserListAdmin from "./UserListAdmin";
import BugReport from "./BugReportsTech";
export default function  AdminPage()  {
 



    return (

      <div className="auth-wrapper">
          <Row>
        <div className="auth-inner-left">
          <h1>Admin options:</h1>
          <hr class="my-4"></hr>
          <Row>

          <ListGroup defaultActiveKey="#link1" as="ol" numbered>
            
          
          
        </ListGroup>
          </Row>
          <br />
          <Row>
            <UserListAdmin/>
            <BugReport/>
          </Row>
          </div>
          <br />
          </Row>
        </div>

    );

}