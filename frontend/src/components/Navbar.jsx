import { Navbar, Nav, Container, NavbarCollapse } from 'react-bootstrap'
import { NavLink } from 'react-router-dom'

function NavbarNav() {
  return (
    <>
      <Navbar>
        <Container>
          <Navbar.Brand as={NavLink} to='/'>Cars</Navbar.Brand>
          <Navbar.Toggle />
          <NavbarCollapse>
            <Nav>
              <Nav.Link as={NavLink} to='/'>Home</Nav.Link>
              <Nav.Link as={NavLink} to='/ads'>Ads</Nav.Link>
              <Nav.Link as={NavLink} to='/cars'>Cars</Nav.Link>
              <Nav.Link as={NavLink} to='/models'>Car Models</Nav.Link>
              <Nav.Link as={NavLink} to='/users'>Users</Nav.Link>
              <Nav.Link as={NavLink} to='/profiles'>User Profiles</Nav.Link>
            </Nav>
          </NavbarCollapse>
        </Container>
      </Navbar>
    </>
  )
}

export default NavbarNav