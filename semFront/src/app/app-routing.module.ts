import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

//componentes
import { HomeComponent } from './components/home/home.component';
import { LoginComponent } from './components/user/login/login.component';
import { RegisterComponent } from './components/user/register/register.component';
import { MenuCarritoComponent } from './components/menu-carrito/menu-carrito.component';
import { MenuEstudiosComponent } from './components/menu-estudios/menu-estudios.component';
import { MenuListaComponent } from './components/menu-lista/menu-lista.component';
import { MenuPerfilComponent } from './components/menu-perfil/menu-perfil.component';
import { MenuPromocionesComponent } from './components/menu-promociones/menu-promociones.component';
import { Page404Component } from './components/page404/page404.component';
import { HumansComponent } from './components/humans/humans.component';
import { ConfirmacionComponent } from './components/confirmacion/confirmacion.component';


const routes: Routes = [
  {path: '', component: LoginComponent },
  {path: 'login', component: LoginComponent },
  {path: 'registro', component: RegisterComponent },
  {path: 'inicio/', component: HomeComponent },
  {path: 'inicio/carrito', component: MenuCarritoComponent },
  {path: 'inicio/estudios', component: MenuEstudiosComponent },
  {path: 'inicio/lista', component: MenuListaComponent },
  {path: 'inicio/perfil', component: MenuPerfilComponent },
  {path: 'inicio/promociones', component: MenuPromocionesComponent },
  {path: 'humans', component: HumansComponent },
  {path: 'confirmacion', component: ConfirmacionComponent },
  {path: '**', component: Page404Component }
]; 

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
  
