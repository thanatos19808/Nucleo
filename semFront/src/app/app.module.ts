import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { LoginComponent } from './components/user/login/login.component';
import { RegisterComponent } from './components/user/register/register.component';
import { HomeComponent } from './components/home/home.component';
import { ConfirmacionComponent } from './components/confirmacion/confirmacion.component';
import { HumansComponent } from './components/humans/humans.component';
import { NavbarComponent } from './components/navbar/navbar.component';
import { Page404Component } from './components/page404/page404.component';
import { MenuCarritoComponent } from './components/menu-carrito/menu-carrito.component';
import { MenuListaComponent } from './components/menu-lista/menu-lista.component';
import { MenuPromocionesComponent } from './components/menu-promociones/menu-promociones.component';
import { MenuEstudiosComponent } from './components/menu-estudios/menu-estudios.component';
import { MenuPerfilComponent } from './components/menu-perfil/menu-perfil.component';

// services
import {DataApiService} from 'src/app/services/data-api.service';


@NgModule({
  declarations: [
    AppComponent,
    LoginComponent,
    RegisterComponent,
    HomeComponent,
    ConfirmacionComponent,
    HumansComponent,
    NavbarComponent,
    Page404Component,
    MenuCarritoComponent,
    MenuListaComponent,
    MenuPromocionesComponent,
    MenuEstudiosComponent,
    MenuPerfilComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule
  ],
  providers: [
   DataApiService
 ],
  bootstrap: [AppComponent]
})
export class AppModule { }
